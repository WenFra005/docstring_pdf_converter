from fpdf import FPDF
from docstring_pdf_converter.generate_pdf import extract_docstrings, generate_cover, docstrings_to_pdf
from docstring_pdf_converter import exemplo


def test_extract_docstrings():

    docstrings = extract_docstrings(exemplo)
    assert "1.   docstring_pdf_converter.exemplo" in docstrings
    assert "1.1    ClasseExemplo" in docstrings
    assert "1.1.1   __init__" in docstrings
    assert "1.1.1   metodo_exemplo" in docstrings
    assert "1.1     funcao_exemplo" in docstrings

def test_generate_cover():
    pdf = FPDF()
    cover_info = {
        "title": "Documentação do projeto",
        "subtitle": "Conversão de docstring para PDF",
        "institution": "",
        "city": "São Paulo",
        "year": "2025"
    }
    generate_cover(pdf, cover_info)
    assert pdf.page_no() == 1

def test_docstrings_to_pdf():
    pdf = FPDF()
    docstrings = "1.    exemplo\n1.1    ExampleClass\n1.1.1     example_method\nDocstring do método."
    docstrings_to_pdf(pdf, docstrings)
    assert pdf.page_no() == 1
