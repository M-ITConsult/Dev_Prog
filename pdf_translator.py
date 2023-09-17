import PyPDF2
from googletrans import Translator
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def translate_pdf(file_path, target_lang):
    # Open the PDF file in read-binary mode
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        translator = Translator()

        translated_pages = []
        # Extract text from each page and translate
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()

            # Translate the extracted text
            translation = translator.translate(page_text, dest=target_lang)
            translated_pages.append(translation.text)

        return translated_pages

def create_translated_pdf(original_pdf_path, translated_pages, target_pdf_path):
    # Create a new PDF file
    c = canvas.Canvas(target_pdf_path, pagesize=letter)

    # Set font and size for the translated text
    c.setFont("Helvetica", 12)

    # Write the translated text on each page of the PDF
    for translated_text in translated_pages:
        c.drawString(50, 750, translated_text)  # Adjust the coordinates as needed
        c.showPage()

    c.save()

# Provide the path to the original PDF file and the target language code
pdf_path = '.pdf'
target_language = 'fr'  # French

# Translate the PDF
translated_pages = translate_pdf(pdf_path, target_language)

# Provide the path to the output translated PDF file
translated_pdf_path = 'pdf.pdf'

# Create the translated PDF
create_translated_pdf(pdf_path, translated_pages, translated_pdf_path)

print("Translated PDF created successfully.")
