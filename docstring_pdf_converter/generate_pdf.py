import inspect
from config import PDF_CONFIG

def extract_docstrings(module):
    docstrings = []
    for name, obj in inspect.getmembers(module):
        if inspect.isfunction(obj) or inspect.isclass(obj):
            docstring = inspect.getdoc(obj)
            if docstring:
                docstrings.append(f"{name}:\n{docstring}\n")
    return "\n".join(docstrings)

def generate_cover(pdf, title: str, subtitle: str, institution: str, city: str, year: str):
    pdf.set_auto_page_break(auto=False)

    pdf.set_left_margin(PDF_CONFIG["margin_left"])
    pdf.set_top_margin(PDF_CONFIG["margin_top"])
    pdf.set_right_margin(PDF_CONFIG["margin_right"])

    pdf.add_page()

    pdf.set_font(PDF_CONFIG["font"], "B", PDF_CONFIG["font_size"])
    pdf.cell(0, 10, f"{institution.upper() if institution else 'AUTOR INDEPENDENTE'}", ln=True, align="C")

    # Pular 8 linhas
    for _ in range(8):
        pdf.ln(10)

    pdf.cell(0, 10, f"{title.upper()}", ln=True, align="C")
    pdf.set_font("Times", "", 12)
    pdf.cell(0, 10, f"{subtitle}", ln=True, align="C")

    # Calcular a posição para a cidade e o ano
    pdf.set_font(PDF_CONFIG["font"], "B", PDF_CONFIG["font_size"])
    page_height = pdf.h - PDF_CONFIG["margin_bottom"]
    pdf.set_y(page_height - 20)
    pdf.set_font(PDF_CONFIG["font"], "B", PDF_CONFIG["font_size"])
    pdf.cell(0, 10, f"{city.upper()}", ln=True, align="C")
    pdf.cell(0, 10, f"{year}", ln=True, align="C")

def docstrings_to_pdf(pdf, docstrings):
    pdf.add_page()
    pdf.set_auto_page_break(auto=PDF_CONFIG["auto_page_break"], margin=PDF_CONFIG["break_margin"])
    pdf.set_font(PDF_CONFIG["font"], size=PDF_CONFIG["font_size"])

    for line in docstrings.split('\n'):
        pdf.multi_cell(0, 10, line)