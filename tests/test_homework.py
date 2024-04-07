import os

from zipfile import ZipFile
from pypdf import PdfReader
from openpyxl import load_workbook
from tests.conftest import ARCHIVE


def test_pdf():
    with ZipFile(ARCHIVE, 'r') as zip_file:
        with zip_file.open('PDF.pdf', 'r') as pdf_file:
            reader = PdfReader(pdf_file)
            text_found = False
            for page_num, page in enumerate(reader.pages, 1):
                page_text = page.extract_text()
                if 'Roman Luzin' in page_text:
                    text_found = True
                    break
                else:
                    print(f"Text not found in page {page_num}: {page_text}")
            assert text_found, "Text 'Roman Luzin' not found in PDF"


def test_xlsx():
    with ZipFile(ARCHIVE, 'r') as zip_file:
        with zip_file.open('Excel.xlsx', 'r') as xlsx_file:
            workbook = load_workbook(xlsx_file)
            sheet = workbook.active
            assert sheet['B9'].value == 'Тест фавикона', "Text 'Тест фавикона' not found in cell B9"


def test_csv():
    file_size_bytes = os.path.getsize(ARCHIVE)
    file_size_mb = file_size_bytes / (1024 * 1024)
    rounded_file_size_mb = round(file_size_mb, 2)
    expected_size_mb = 1.55
    assert rounded_file_size_mb == expected_size_mb, f"CSV file size is not approximately 1.55 MB (rounded to nearest MB)"
