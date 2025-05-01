from pdf2docx import Converter

old_pdf = "University.pdf"
new_doc = "new_word.docx"

obj = Converter(old_pdf)
obj.convert(new_doc)
obj.close()
