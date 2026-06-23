from utils.pdf_reader import read_pdf

text = read_pdf("data/test.pdf")

print(text[:1000])