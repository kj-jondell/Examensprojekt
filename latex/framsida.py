from pdfrw import PdfReader, PdfWriter

mall = PdfReader('Mall.pdf')
text = PdfReader('kandidat.pdf')

writer = PdfWriter()
writer.addpage(mall.pages[0])
writer.addpage(mall.pages[1])
for page in text.pages:
    writer.addpage(page)
writer.addpage(mall.pages[2])
writer.write('KarlJohannesKandidat.pdf')

