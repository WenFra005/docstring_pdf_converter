from fpdf import FPDF

def generate_cover(title: str, subtitle: str, institution: str, city: str, year: str, output_file: str):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=False)
    pdf.add_page()

    pdf.set_left_margin(30)
    pdf.set_top_margin(30)
    pdf.set_right_margin(20)

    pdf.set_font("Times", "B", 12)
    pdf.cell(0, 10, f"{institution.upper() if institution else 'AUTOR INDEPENDENTE'}", ln=True, align="C")

    # Pular 8 linhas
    for _ in range(8):
        pdf.ln(10)

    pdf.cell(0, 10, f"{title.upper()}", ln=True, align="C")
    pdf.set_font("Times", "", 12)
    pdf.cell(0, 10, f"{subtitle}", ln=True, align="C")

    # Calcular a posição para a cidade e o ano
    pdf.set_font("Times", "B", 12)
    page_height = pdf.h - pdf.b_margin
    pdf.set_y(page_height - 20)
    pdf.set_font("Times", "", 12)
    pdf.cell(0, 10, f"{city.upper()}", ln=True, align="C")
    pdf.cell(0, 10, f"{year}", ln=True, align="C")

    pdf.output(output_file)

generate_cover(
    "Documentação do projeto",
    "Conversão de docstring para PDF",
    "",
    "São Paulo",
    "2025",
    "capa.pdf"
)