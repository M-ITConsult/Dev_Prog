import csv
import re
from docx import Document

def extract_links_from_docx(docx_file):
    document = Document(docx_file)
    links = []

    for element in document.element.body.iter():
        if element.tag.endswith(('t', 'p')):
            text = element.text
            if text:
                matches = re.findall(r'https?://[^\s]+', text)
                links.extend(matches)

    return links

def save_links_to_csv(links, csv_file):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)

        for link in links:
            writer.writerow([link])

# Usage example
docx_file_path = input('Your .docx document: ')
csv_file_path = 'links.csv'

links = extract_links_from_docx(docx_file_path)
save_links_to_csv(links, csv_file_path)