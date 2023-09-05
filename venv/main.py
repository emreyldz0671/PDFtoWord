from pdf2docx import parse

parse(pdf_file="../MüzikEtkinlikleri.pdf", docx_file="../Muzik.docx", start=0, end=None)

#Bir diğer yöntem:

#from pdf2docx import Converter

#pdf_path = "sample.pdf"
#docx_path = "sample.docx"

#cv = Converter(pdf_file=pdf_path)
#cv.Converter(docx_filename=docx.path)
#cv.close()