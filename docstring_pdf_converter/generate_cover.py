import os

from fpdf import FPDF

def generate_cover (title: str, subtitle: str, author: str, output_file: str):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()

    pdf.set_left_margin(30)
    pdf.set_top_margin(30)
    pdf.set_right_margin(20)

    pdf.set_font("Times", "B", 16)
    pdf.cell(0, 40, title, ln=True, align="C")

    pdf.set_font("Times", "I", 14)
    pdf.cell(0, 20, subtitle, ln=True, align="C")

    pdf.set_font("Times", "", 12)
    pdf.ln(50)
    pdf.cell(0, 10, f"Author: {author}", ln=True, align="C")

    pdf.output(output_file)

    generate_cover(
        "Documentação do projeto",
        "Conversão de docstring para PDF",
        "Wendell Francisco",
        "capa.pdf")