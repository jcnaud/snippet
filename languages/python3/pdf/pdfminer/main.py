# coding: utf-8

## Source : https://lobstr.io/index.php/2018/07/30/scraping-document-pdf-python-pdfminer/

import os
from io import BytesIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.pdfpage import PDFPage

def pdf2txt(path):
    """
    Extract text from PDF file, and return
    the string contained inside
 
    :param path (str) path to the .pdf file
    :return: text (str) string extracted
    """
 
    rsrcmgr = PDFResourceManager()
    retstr = BytesIO()
    device = TextConverter(rsrcmgr, retstr)
    with open(path, "rb") as fp:  # open in 'rb' mode to read PDF bytes
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.get_pages(fp, check_extractable=True):
            interpreter.process_page(page)
        device.close()
        text = retstr.getvalue()
        retstr.close()
    return text.decode('utf-8')


def main():
    print(pdf2txt('./simple1.pdf'))

    

if __name__ == '__main__':
    main()
