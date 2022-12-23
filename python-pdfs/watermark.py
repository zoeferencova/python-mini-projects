from PyPDF2 import PdfFileReader, PdfFileWriter
import sys

filename = sys.argv[1]
reader = PdfFileReader('wtr.pdf')
watermark = reader.pages[0]
writer = PdfFileWriter()

reader = PdfFileReader(filename)
page_indices = list(range(0, len(reader.pages)))

for i in page_indices:
    content_page = reader.pages[i]
    mediabox = content_page.mediaBox
    content_page.mergePage(watermark)
    content_page.mediaBox = mediabox
    writer.addPage(content_page)

with open(filename, 'wb') as fp:
    writer.write(fp)


# Given solution
filename = sys.argv[1]
template = PdfFileReader(open(filename, 'rb'))
watermark = PdfFileReader(open('wtr.pdf', 'rb'))
output = PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

with open('watermarked_output.pdf', 'wb') as file:
    output.write(file)
