import sys, re , io, typing
from collections.abc import Iterable
import traceback
import json
import fitz
from PIL import Image


class ExtractElFromPdf():
    """класс для извлечения элементов из  pdf  файла"""

    def __init__(self):
        self.doc: fitz.Document = None
        self.page: fitz.Page = None

    def get_doc(self, path: str) -> fitz.Document:
        try:
            doc = fitz.open(path)
            # for i in range(len(doc)):
            #     for img in doc.getPageImageList(i):
            #         xref = img[0]
            #         pix = fitz.Pixmap(doc, xref)
            #         if pix.n < 5:       # this is GRAY or RGB
            #             pix.writePNG("p%s-%s.png" % (i, xref))
            #         else:               # CMYK: convert to RGB first
            #             pix1 = fitz.Pixmap(fitz.csRGB, pix)
            #             pix1.writePNG("p%s-%s.png" % (i, xref))
            #             pix1 = None
            #         pix = None
            return doc
        except:
            return None

    def get_page(self, doc: fitz.Document, num_page: str) -> fitz.Page:
        
        if doc is not None:
            try:
                page = doc.load_page(num_page)
                return page
            except:
                return None
        else:
            return None
            

    def ex_draw(self, page: fitz.Page) -> list:
        return page.get_drawings()

    def ex_text(self, page: fitz.Page) -> list:
        # print(len(page.get_text("dict")["blocks"]))
        return page.get_text("dict", flags=11)["blocks"]
        # return page.get_text_blocks("dict")

    def ex_image(self, doc: fitz.Document, page: fitz.Page) -> list:
        list_images = []      
        image_list = page.get_images()
        # img_info = page.get_image_info()
        # img_rect = page.get_image_rects()
        # print(img_info)
        # print(img_rect)
        for image_index, img in enumerate(image_list, start=1):
            image = {}
            img_xref = img[0]
            img_name = img[7]
            image["img"] = img
            image["base_image"] = doc.extract_image(img_xref)
            image["bbox"], image["transform"] = page.get_image_bbox(img_name, transform=True)
            # image[""]
            # print(img)
            # (10, 0, 4000, 4000, 8, 'DeviceRGB', '', 'FXX1', 'DCTDecode')  
            # print(base_image.keys())
            # dict_keys(['ext', 'smask', 'width', 'height', 'colorspace', 'bpc', 'xres', 'yres', 'cs-name', 'image'])
            # print(bbox)
            # Rect(363.0459899902344, 586.7990112304688, 561.468017578125, 774.1580200195312)
            # print(transform)
            # Matrix(198.4219970703125, 0.0, -0.0, 187.35899353027344, 363.0459899902344, 586.7990112304688)
           

            # img_name = img[7]
            # img_width = img[2]
            # img_height = img[3]
            # imgrect = fitz.Rect(0,0,img_width,img_height)
            # base_image = doc.extract_image(img_xref)
            # # print(base_image.keys())
            # print("ext", type(base_image["ext"]), base_image["ext"])
            # print("smask", type(base_image["smask"]), base_image["smask"])
            # print("width", type(base_image["width"]), base_image["width"])
            # print("height", type(base_image["height"]), base_image["height"])
            # print("colorspace", type(base_image["colorspace"]), base_image["colorspace"])
            # print("bpc", type(base_image["bpc"]), base_image["bpc"])
            # print("xres", type(base_image["xres"]), base_image["xres"])
            # print("yres", type(base_image["yres"]), base_image["xres"])
            # print("cs-name", type(base_image["cs-name"]), base_image["cs-name"])
            # print("image", type(base_image["image"]))
            # dict_keys(['ext', 'smask', 'width', 'height', 'colorspace', 'bpc', 'xres', 'yres', 'cs-name', 'image'])
            # image_bytes = base_image["image"]
            # image_ext = base_image["ext"]
            # image = Image.open(io.BytesIO(image_bytes))
            # image.save(open(f"out_file/image_{image_index}.{image_ext}", "wb"))
            # print(image)
            list_images.append(image)
        return list_images

#         import fitz
# from icecream import ic
# from matrix_property import matprop

# file = 'd:/py/base/test/投标文件.pdf'
# pdf = fitz.open(file)
# page = pdf[0]

# img = page.get_images()[0]
# ic(img)
# xref = img[0]
# img_name = img[7]
# img_width = img[2]
# img_height = img[3]
# imgrect = fitz.Rect(0,0,img_width,img_height)
# ic(imgrect)
# shrink = fitz.Matrix(1/img_width,0,0,1/img_height,0,0)
# ic(shrink)
# bbox, transform = page.get_image_bbox(img_name, transform=True)
# ic(bbox)
# ic(transform)
# ic(imgrect*shrink*transform)

# img = pdf.extract_image(xref)
# img_data = img["image"]
# pix = fitz.Pixmap(img["image"])

# img_pix = fitz.Pixmap(pdf,xref)
# ic(img_pix)
# ic(matprop(transform))

    def get_el(self, doc: fitz.Document, page: fitz.Page) -> dict[str ,tuple, list]:
        # for box in  page.get_bboxlog
        # rl = page.search_for("R-01")
        # box = page.get_textbox(rl[0])
        # print(rl, box)
        
        el = {}
        bound = page.bound()
        # print(type((bound.x0, bound.y0, bound.width, bound.height)))
        el["rect"] = (bound.x0, bound.y0, bound.width, bound.height)
        el["draw"] = self.ex_draw(page)
        el["text"] = self.ex_text(page)
        el["image"] = self.ex_image(doc, page)
        return el




