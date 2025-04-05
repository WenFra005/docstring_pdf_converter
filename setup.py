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
    description="Uma ferramenta para converter docstrings de módulos Python em PDFs formatados.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/WenFra005/docstring_pdf_converter",
    author="Wendell Francisco",
    author_email="wendellfrancisco2005@hotmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.6",
    include_package_data=True,
    package_data={
        "": ["*.txt", "*.py"],
        "docstring_pdf_converter": ["data/*.txt"],
    },
    tests_require=["pytest"]
)
