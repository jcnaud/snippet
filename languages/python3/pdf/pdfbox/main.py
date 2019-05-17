# coding: utf-8
## Source : https://pypi.org/project/python-pdfbox/

import pdfbox

def main():
    import pdfbox
    p = pdfbox.PDFBox()
    text = p.extract_text('./simple1.pdf')
    print('--------------------')
    print(text)

if __name__ == '__main__':
    main()
