from PIL import Image
import img2pdf
import os

image_path = "images/image_2.jpg"
pdf_path = "pdf/image_2.pdf"

image = Image.open(image_path)

pdf_bytes = img2pdf.convert(image.filename)

file = open(pdf_path, "wb")

file.write(pdf_bytes)

image.close()

file.close()
