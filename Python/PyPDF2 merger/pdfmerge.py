# Very useful tool to merge PDF files on the go without requiring Acrobat Pro. 

from PyPDF2 import PdfFileMerger

pdfs = ['file1.pdf', 'file2.pdf'] 

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()