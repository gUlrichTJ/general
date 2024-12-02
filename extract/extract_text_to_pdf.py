# -*- coding: utf-8 -*-

import PyPDF2

def extract_text_from_pdf(pdf_path, pages_per_batch=10):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        total_pages = len(reader.pages)

        for i in range(0, total_pages, pages_per_batch):
            text = ""
            for j in range(i, min(i + pages_per_batch, total_pages)):
                text += reader.pages[j].extract_text() + "\n"
                
            #print(f"Texte extrait de la page {i + 1} à {min(i + pages_per_batch, total_pages)} :")
            print(text)
            print("-------------------------------------------------")


def extract_text_from_pdf2(pdf_path, output_path, pages_per_batch=10):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        # Check if reader.pages is valid
        if not hasattr(reader, 'pages'):
            print("Error: Unable to read pages from PDF.")
            return
        
        total_pages = len(reader.pages)

        # Ensure total_pages is an integer
        if not isinstance(total_pages, int):
            print("")
            return

        with open(output_path, 'w', encoding='utf-8') as output_file:
            for i in range(0, total_pages, pages_per_batch):
                text = ""
                for j in range(i, min(i + pages_per_batch, total_pages)):
                    text += reader.pages[j].extract_text() + "\n"
                
                # Write the extracted text to the file
                output_file.write("hihihi")
                output_file.write(text)
                output_file.write("_______________________________\n")
                output_file.write("______________________________________________________________________\n")

if __name__ == "__main__":
    pdf_path = 'fr-covid-19_recovery_framework_for_africa.pdf'  # Spécifiez le chemin de votre PDF
    extract_text_from_pdf(pdf_path)

    output_path = 'extract.txt'  # Nom du fichier de sortie
    extract_text_from_pdf2(pdf_path, output_path)

