"""
Este módulo contém a função principal para gerar um PDF a partir de docstrings de um módulo Python.
"""
from datetime import datetime
from fpdf import FPDF
from docstring_pdf_converter.generate_pdf import generate_cover, extract_docstrings, docstrings_to_pdf

def main():
    """
    Função principal que gera um PDF a partir de docstrings extraídas de um módulo Python.

    :return: None
    """
    pdf = FPDF()

    title = input("Digite o título do documento: ")
    subtitle = input("Digite o subtítulo do documento: ")
    institution = input("Digite a instituição (deixe em branco se não houver): ")
    city = input("Digite a cidade: ")

    cover_info = {
        "title": title,
        "subtitle": subtitle,
        "institution": institution,
        "city": city,
        "year": datetime.now().year
    }

    generate_cover(pdf, cover_info)

    module_name = "exemplo"
    module = __import__(module_name)
    docstrings = extract_docstrings(module)
    docstrings_to_pdf(pdf, docstrings)

    pdf.output("documentacao_completa.pdf")

if __name__ == "__main__":
    main()
