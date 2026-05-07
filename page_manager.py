import os
import webbrowser


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PAGES_DIR = os.path.join(BASE_DIR, "pages")


def open_page(page_number):

    file_name = f"page{page_number}.html"

    file_path = os.path.join(PAGES_DIR, file_name)

    if os.path.exists(file_path):

        webbrowser.open(f"file://{os.path.abspath(file_path)}")

        return True

    return False