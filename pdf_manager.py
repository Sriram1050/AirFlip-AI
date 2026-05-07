import fitz
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PDF_PATH = os.path.join(
    BASE_DIR,
    "documents",
    "sample.pdf"
)

OUTPUT_DIR = os.path.join(BASE_DIR, "temp_pages")

os.makedirs(OUTPUT_DIR, exist_ok=True)


def open_pdf_page(page_number):

    if not os.path.exists(PDF_PATH):
        print("PDF file not found")
        return False

    doc = fitz.open(PDF_PATH)

    total_pages = len(doc)

    print("Total PDF Pages:", total_pages)

    if page_number < 1 or page_number > total_pages:
        print("Invalid page number:", page_number)
        return False

    page = doc.load_page(page_number - 1)

    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))

    output_path = os.path.join(
        OUTPUT_DIR,
        f"page_{page_number}.png"
    )

    pix.save(output_path)

    os.startfile(output_path)

    return True