from pypdf import PdfWriter
merger = PdfWriter()
for pdf in ['Pdf\\a.pdf','Pdf\\b.pdf']:
    merger.append(pdf)
merger.write("merged-pdf.pdf")
merger.close()