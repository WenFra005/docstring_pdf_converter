"""
Configuração do setup.py para o projeto docstring_pdf_converter.
"""

from setuptools import setup, find_packages

setup(
    name="docstring_pdf_converter",
    version="0.1",
    packages=find_packages(),
    install_requires=["fpdf"],
    entry_points={
        "console_scripts": [
            "docstring-pdf-converter = docstring_pdf_converter.main.py",
        ]
    },
)
