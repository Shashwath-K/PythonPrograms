from PyPDF2 import PdfWriter,PdfReader

num=int(input("Enter the page number you want to combine from: "))

pdf1=open('birds.pdf','rb')
pdf2=open('birdspic.pdf','rb')

pdf_writer=PdfWriter()

pdf1_reader=PdfReader(pdf1)
page=pdf1_reader.pages[num-1]
pdf_writer.add_page(page)

pdf2_reader=PdfReader(pdf2)
page=pdf2_reader.pages[num-1]
pdf_writer.add_page(page)

var = "Output{}.pdf".format(num)

with open(var,'wb') as output:
    pdf_writer.write(output)

if not output:
    print(var,"Not Created")
else:
    print(var,"Successfully created")
