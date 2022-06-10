from PIL import Image
import pytesseract
from sciHub_parse import SH_parse
import pdf2image
import pytesseract
import numpy as np
class OCR:
    @staticmethod
    def pdf2imgs(pdf):
        images = pdf2image.convert_from_bytes(pdf)
        return images
        

if __name__ == "__main__":
    parser = SH_parse()
    pdf_bytes = parser.next_pdf(save=False)
    images = OCR.pdf2imgs(pdf_bytes['pdf'])
    for i in images:
        print(pytesseract.image_to_string(np.array(i), config='--psm 6'))
        i.show()

    