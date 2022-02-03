# Importing the necessary modules
from fpdf import FPDF
from PIL import Image
import img2pdf
import os
import glob

# Including the FPDF() function which is responsible to generate the pdf
pdf = FPDF()

# imagelist is the list with all image filenames
imagelist = glob.glob("images_watermarked/*.*")

# This loop is responsible for taking images and convert them into pdf
for image in imagelist:
    pdf.add_page()
    pdf.image(image, 0, 0, 210, 297)

# And at last all the images that are converted into pdf will be stored inside one single pdf file.
pdf.output("pdf/yourfile.pdf", "F")
