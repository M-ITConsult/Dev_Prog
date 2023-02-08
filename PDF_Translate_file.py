# PDF Translate file

import PyPDF2
import goslate

def translate_to_french(sentence):
    gs = goslate.Goslate()
    return gs.translate(sentence, 'fr')

def translate_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    pdf_text = ""
    # for page in range(len(pdf_reader.pages)):
    #     pdf_text += pdf_reader.pages[page].extract_text()
    # translated_text = translate_to_french(pdf_text)
    # print("Translation:")
    # print(translated_text)
# Save to in new PDF
    for page in range(len(pdf_reader.pages)):
        pdf_text += pdf_reader.pages[page].extract_text()
        translated_text = translate_to_french(pdf_text)
        pdf_writer = PyPDF2.PdfFileWriter()
        pdf_text_page = PyPDF2.pdf.PageObject.create_pages_from_text(translated_text)
        pdf_writer.addPage(pdf_text_page)
        with open("translated_pdf.pdf", "wb") as outfile:
            pdf_writer.write(outfile)
            print("Translation saved as translated_pdf.pdf")

pdf_file = input("Enter the name of the PDF file: ")
translate_pdf(pdf_file)
