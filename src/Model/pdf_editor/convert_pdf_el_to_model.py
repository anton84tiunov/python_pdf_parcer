import re
from collections import OrderedDict
import fitz
import src.Model.general.draw_model as drawModel
import src.Model.general.text_model as textModel
import src.Model.general.image_model as imageModel


class ConvertPdfElToModel():

    def convert_dashes(self, dashes: str) -> tuple[list[float], int]:
        list_str_dashes_pattern = "[]"
        str_dashes_offset = "0"
        # print(type(dashes), dashes)
        if  isinstance(dashes, str):
            if "[" in dashes and "]" in dashes:
                list_str_dashes_pattern = re.search(r'^\[[ 0-9\.]*\]', dashes).group(0).replace("[ ", "").replace(" ]", "").split(' ')
            if any(map(str.isdigit, dashes)):
                str_dashes_offset_0 = re.search(r'\] [\d]*$', dashes)
                if str_dashes_offset_0 is not None:
                    str_dashes_offset = str_dashes_offset_0.group(0).replace("] ", "")
        dashes_pattern = []
        dashes_offset = 0
        if list_str_dashes_pattern is not None and any(map(str.isdigit, list_str_dashes_pattern)): 
            dashes_pattern = list(map(float, list_str_dashes_pattern))
            # for d_p in range(len(dashes_pattern)):
            if dashes_pattern[0] == 0.0:
                dashes_pattern[0] = 1.0
                dashes_pattern[1] = 1.0
        if  str_dashes_offset.isdigit():
            dashes_offset = int(str_dashes_offset)
        return dashes_pattern, dashes_offset

    def conv_draw(self, draw) -> drawModel.DrawModel:
        draw_model = drawModel.DrawModel()
        draw_model.type = draw["type"]
        draw_model.color = draw["color"]
        draw_model.fill = draw["fill"]
        draw_model.closePath = draw["closePath"]
        draw_model.even_odd = draw["even_odd"]
        draw_model.seqno = draw["seqno"]
        draw_model.dashes = draw["dashes"]
        draw_model.lineJoin = draw["lineJoin"]
        draw_model.lineCap = draw["lineCap"]
        draw_model.width = draw["width"]
        draw_model.stroke_opacity = draw["stroke_opacity"]
        draw_model.fill_opacity = draw["fill_opacity"]
        
        if draw["items"][0][0] == "re" and len(draw["items"]) == 1:
            draw_model.items.draw = "re"
            p0 = (draw["items"][0][1][0], draw["items"][0][1][1])
            p1 = (draw["items"][0][1][2], draw["items"][0][1][1])
            p2 = (draw["items"][0][1][2], draw["items"][0][1][3])
            p3 = (draw["items"][0][1][0], draw["items"][0][1][3])
            if draw["items"][0][2] > 0:
                draw_model.items.cords.append((p0, p1, p2, p3))
            elif draw["items"][0][2] < 0:
                draw_model.items.cords.append((p0, p3, p2, p1))
        elif draw["items"][0][0] == "qu" and len(draw["items"]) == 1:
            draw_model.items.draw = "qu"
            p0 = (draw["items"][0][1][0][0], draw["items"][0][1][1][1])
            p1 = (draw["items"][0][1][1][0], draw["items"][0][1][1][1])
            p2 = (draw["items"][0][1][2][0], draw["items"][0][1][2][1])
            p3 = (draw["items"][0][1][3][0], draw["items"][0][1][3][1])
            draw_model.items.cords.append((p0, p1, p2, p3))
        else:
            draw_model.items.draw = "pol"
            if draw["closePath"]:
                draw_model.items.draw = "path"
            for dr in draw["items"]:
                if dr[0] == "re":
                    p0 = (dr[1][0], dr[1][1])
                    p1 = (dr[1][2], dr[1][1])
                    p2 = (dr[1][2], dr[1][3])
                    p3 = (dr[1][0], dr[1][3])
                    if dr[2] > 0:
                        draw_model.items.cords.append(("re", (p0, p1, p2, p3)))
                    elif dr[2] < 0:
                        draw_model.items.cords.append(("re", (p0, p3, p2, p1)))
                if dr[0] == "qu":
                    qu = True
                    p0 = (dr[1][0][0], dr[1][0][1])
                    p1 = (dr[1][1][0], dr[1][1][1])
                    p2 = (dr[1][2][0], dr[1][2][1])
                    p3 = (dr[1][3][0], dr[1][3][1])
                    draw_model.items.cords.append(("qu", (p0, p1, p2, p3, p0)))
                if dr[0] == "l":
                    l = True
                    p0 = (dr[1][0], dr[1][1])
                    p1 = (dr[2][0], dr[2][1])
                    draw_model.items.cords.append(("l", (p0, p1)))
                if dr[0] == "c":
                    c = True
                    p0 = (dr[1][0], dr[1][1])
                    p1 = (dr[2][0], dr[2][1])
                    p2 = (dr[3][0], dr[3][1])
                    p3 = (dr[4][0], dr[4][1])
                    draw_model.items.cords.append(("c", (p0, p1, p2, p3)))

        return draw_model

    def conv_text(self, block) -> textModel.TextModel:
        
        text_model = textModel.TextModel()
        text_line = textModel.TextLine()
        text_spane = textModel.TextSpane()
        text_model.block_number = block["number"] # 0
        text_model.block_type = block["type"] # 0
        text_model.block_bbox = block["bbox"] # (43.0, 36.177734375, 207.52720642089844, 58.326171875)
        block_lines = block["lines"]
        for line in block_lines:
            text_line.line_wmode = line["wmode"] # 0
            text_line.line_dir = line["dir"] # (1.0, 0.0)
            text_line.line_bbox = line["bbox"] # (43.0, 36.177734375, 207.52720642089844, 58.326171875)
            line_spans = line["spans"]
            for span in line_spans:
                text_spane.span_size = span["size"] # 20.0
                text_spane.span_flags =  span["flags"] # 4
                text_spane.span_font = span["font"] # 'Times New Roman'
                text_spane.span_color = fitz.sRGB_to_rgb(span["color"]) # 0
                text_spane.span_ascender = span["ascender"] # 0.89111328125   восходящий
                text_spane.span_descender = span["descender"] # -0.21630859375 спусковое устройство
                text_spane.span_text = span["text"] # 'Пример PDF файла'
                text_spane.span_origin = span["origin"] # (43.0, 54.0)
                text_spane.span_bbox = span["bbox"] # (43.0, 36.177734375, 207.52720642089844, 58.326171875)
                
                text_line.line_spans.append(text_spane)
            text_line.line_spans = list(OrderedDict.fromkeys(text_line.line_spans))
            text_model.block_lines.append(text_line)
        text_model.block_lines = list(OrderedDict.fromkeys( text_model.block_lines))
        
        return text_model

#     a = span["ascender]
# d = span["descender"]
# r = fitz.Rect(span["bbox"])
# o = fitz.Point(span["origin"])  # its y-value is the baseline
# r.y1 = o.y - span["size"] * d / (a - d)
# r.y0 = r.y1 - span["size"]
# # r now is a rectangle of height 'fontsize'

    def conv_image(self, image) -> imageModel.ImageModel:
        b_img_model = imageModel.BaseImageModel()
        img_model = imageModel.ImageModel()

        # print(image)
        b_img_model.ext = image['base_image']["ext"]
        b_img_model.bpc = image["base_image"]["bpc"]
        b_img_model.smask = image["base_image"]["smask"]
        b_img_model.width = image["base_image"]["width"]
        b_img_model.height = image["base_image"]["height"]
        b_img_model.xres = image["base_image"]["xres"]
        b_img_model.yres = image["base_image"]["yres"]
        b_img_model.colorspace = image["base_image"]["colorspace"]
        b_img_model.cs_name = image["base_image"]["cs-name"]
        b_img_model.image = image["base_image"]["image"]

        img_model.base_image = b_img_model
        img_model.img = image["img"]
        img_model.bbox = image["bbox"]
        img_model.matrix = image["transform"]

        return img_model





    def conv_draws(self, draws: list) -> list[drawModel.DrawModel]:
        draws_model = []
        for draw in draws:
            draw_model = self.conv_draw(draw)
            draws_model.append(draw_model)
        return draws_model

    def conv_texts(self, texts: list) -> list[textModel.TextModel]:
        texts_model = []
        # print(len(texts))
        for text in texts:
            text_model = self.conv_text(text)
            # print(text_model.block_number)
            texts_model.append(text_model)
        return texts_model

    def conv_images(self, images: list) -> list[imageModel.ImageModel]:
        
        images_model: list[imageModel.ImageModel] = []
        for image in images:
            # print(image)
            image_model = self.conv_image(image)
            images_model.append(image_model)
        return images_model


































