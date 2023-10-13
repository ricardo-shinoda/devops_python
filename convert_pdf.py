import PyPDF2
import json
import os


def unlock_pdf(pdf_file_path, password, output_path):
    with open(pdf_file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        if pdf_reader.is_encrypted:
            pdf_reader.decrypt(password)
        pdf_writer = PyPDF2.PdfWriter()
        for page_num in range((pdf_reader.numPages)):
            pdf_writer.addPage(pdf_reader.getPage(page_num))
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)


def pdf_to_json(pdf_file_path, json_file_path):
    # Unlock the PDF if it's password-protected
    unlocked_pdf_path = 'unlocked.pdf'
    password = '6993'  # Replace with the actual password
    unlock_pdf(pdf_file_path, password, unlocked_pdf_path)

    # Open the unlocked PDF
    with open(unlocked_pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Initialize an empty list to store page text
        page_texts = []

        # Extract text from each page
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            page_texts.append(page.extract_text())

        # Create a dictionary with the extracted text
        pdf_text = {"pages": page_texts}

        # Convert the dictionary to JSON
        json_data = json.dumps(pdf_text, indent=4)

        # Write the JSON data to a file
        with open(json_file_path, 'w') as json_file:
            json_file.write(json_data)


if __name__ == "__main__":
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_file_name = "2023-09.pdf"  # PDF file name
    # Construct the absolute path
    pdf_file_path = os.path.join(script_dir, pdf_file_name)
    json_file_path = "output.json"  # Replace with the desired JSON output file path

    pdf_to_json(pdf_file_path, json_file_path)
