import unittest
# import ..src.Model.pdf_editor.convert_pdf_el_to_model as convert_pdf_el_to_model
import  src.Model.pdf_editor.convert_pdf_el_to_model as convert_pdf_el_to_model

class TestTest1(unittest.TestCase):
    
    def setUp(self):
        self.test_convert_pdf_el_to_model = convert_pdf_el_to_model.ConvertPdfElToModel()

    # def test_convert_dashes(self):
    #    self.assertEqual(self.test_convert_pdf_el_to_model.convert_dashes("[ 0.3 0.4 ] 0.1"), tuple[list[float], int])

    def test_convert_dashes(self):
        self.assertEqual(self.test_convert_pdf_el_to_model.convert_dashes("[ 3 4 ] 1"),([3.0, 4.0], 1.0))
        self.assertEqual(self.test_convert_pdf_el_to_model.convert_dashes("[] 0"),([], 0.0))
        # self.assertEqual(self.test_convert_pdf_el_to_model.convert_dashes("[ 0 ] 0"),([0.0], 0.0))
        self.assertEqual(self.test_convert_pdf_el_to_model.convert_dashes("[ 4 ] 1"),([4.0], 1.0))
        # self.assertEqual(self.test_convert_pdf_el_to_model.convert_dashes("[0] 0"),([0.0], 0.0))
        # self.assertEqual(self.test_convert_pdf_el_to_model.convert_dashes("[1 2] 7"),([1.0, 2.0], 7.0))

# if __name__ == "__main__":
#   unittest.main()


