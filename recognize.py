import imp
from PIL import Image
import pytesseract
from sciHub_parse import SH_parse

if __name__ == "__main__":
    parser = SH_parse()
    parser.next_pdf(True)
    