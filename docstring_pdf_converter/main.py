"""
Este módulo contém a função principal para gerar um PDF a partir de docstrings de um módulo Python.
"""

from fpdf import FPDF
from generate_pdf import generate_cover, extract_docstrings, docstrings_to_pdf

def main():
    """
    Função principal que gera um PDF a partir de docstrings extraídas de um módulo Python.

    :return: None
    """
    pdf = FPDF()

    generate_cover(
        pdf,
        "Documentação do projeto",
        "Conversão de docstring para PDF",
        "",
        "São Paulo",
        "2025"
    )

    module_name = "exemplo"
    module = __import__(module_name)
    docstrings = extract_docstrings(module)
    docstrings_to_pdf(pdf, docstrings)

    pdf.output("documentacao_completa.pdf")

if __name__ == "__main__":
    main()
