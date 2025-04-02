import unittest
from fpdf import FPDF
from docstring_pdf_converter.generate_pdf import extract_docstrings, generate_cover, docstrings_to_pdf
from docstring_pdf_converter import exemplo


class TestGeneratePDF(unittest.TestCase):

    def test_extract_docstrings(self):

        docstrings = extract_docstrings(exemplo)
        self.assertIn("1.   docstring_pdf_converter.exemplo", docstrings)
        self.assertIn("1.1    ClasseExemplo", docstrings)
        self.assertIn("1.1.1   __init__", docstrings)
        self.assertIn("1.1.1   metodo_exemplo", docstrings)
        self.assertIn("1.1     funcao_exemplo", docstrings)

    def test_generate_cover(self):
        pdf = FPDF()
        generate_cover(pdf, "Título", "Subtítulo", "Instituição", "Cidade", "2025")
        self.assertEqual(pdf.page_no(), 1)

    def test_docstrings_to_pdf(self):
        pdf = FPDF()
        docstrings = "1.    exemplo\n1.1    ExampleClass\n1.1.1     example_method\nDocstring do método."
        docstrings_to_pdf(pdf, docstrings)
        self.assertEqual(pdf.page_no(), 1)

if __name__ == '__main__':
    unittest.main()
