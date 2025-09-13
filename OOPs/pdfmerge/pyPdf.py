from PyPDF2 import PdfWriter as pw

merger=pw()

for pdf in ["OOPs\pdfmerge\EPFO Pension.pdf", "OOPs\pdfmerge\EPFO.pdf", "OOPs\pdfmerge\Form16FY2425.pdf"]:
    merger.append(pdf)

merger.write("OOPs\pdfmerge\merged.pdf")
merger.close()