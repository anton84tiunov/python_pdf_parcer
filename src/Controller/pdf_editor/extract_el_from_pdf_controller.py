import src.View.my_widgets.pdf_editor.interact.pdf_editor_interact as pdf_editor_interact
import src.Model.pdf_editor.extract_el_from_pdf_page as extract_el_from_pdf_page
import src.Model.pdf_editor.convert_pdf_el_to_model as convert_pdf_el_to_model
import src.Model.general.draw_model as drawModel
import src.Model.general.text_model as textModel

class ExtractElFromPdfController():
    def __init__(self):
        self.extr = extract_el_from_pdf_page.ExtractElFromPdf()
        self.conv = convert_pdf_el_to_model.ConvertPdfElToModel()

    def open_pdf(self, path, num_page) -> tuple[list[drawModel.DrawModel], list[textModel.TextModel]]:
        doc = self.extr.get_doc(path)
        page = self.extr.get_page(doc, num_page)
        el =  self.extr.get_el(page)
        el_draw = self.conv.conv_draws(el["draw"])
        el_text = self.conv.conv_texts(el["text"])
        return el_draw, el_text














