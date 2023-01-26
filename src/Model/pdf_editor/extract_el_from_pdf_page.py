import sys, re , io, typing
from collections.abc import Iterable
import traceback
import json
import fitz


class ExtractElFromPdf():
    """класс для извлечения элементов из  pdf  файла"""

    def __init__(self):
        self.doc: fitz.Document = None
        self.page: fitz.Page = None

    def get_doc(self, path: str) -> fitz.Document:
        try:
            doc = fitz.open(path)
            return doc
        except:
            return None

    def get_page(self, doc: fitz.Document, num_page: str) -> fitz.Page:
        if doc is not None:
            try:
                page = doc.load_page(num_page)
                # print(len(page.get_text("dict")["blocks"]))
                # for bno, block in enumerate(page.get_text("dict", flags=0)["blocks"]):
                #     print("block number:", bno)
                # for i in page.get_text():
                #     print(i)
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

    def ex_image(self, page: fitz.Page) -> list:
        return page.get_images()

    def get_el(self, page: fitz.Page) -> dict[str ,list]:
        el = {}
        el["draw"] = self.ex_draw(page)
        el["text"] = self.ex_text(page)
        el["image"] = self.ex_image(page)
        return el




