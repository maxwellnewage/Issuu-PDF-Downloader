import os
from fpdf import FPDF
from PIL import Image


def creator(pdflist, pdf_filename):
    pdf = FPDF()
    print(f'Started {pdf_filename} creation...')

    for imageFile in pdflist:
        cover = Image.open(imageFile)
        width, height = cover.size

        # convert pixel in mm with 1px=0.264583 mm
        width, height = float(width * 0.264583), float(height * 0.264583)

        pdf.add_page(format=(width, height))

        pdf.image(imageFile, 0, 0, width, height)

    filename_with_folder = os.path.join('./pdfs/', pdf_filename)
    pdf.output(filename_with_folder, "F")

    print('Completed pdf creation...')
