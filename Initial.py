import PyPDF2
import json
import os


def pdf_to_json(pdf_file_path, json_file_path):
    # Open the PDF file
    with open(pdf_file_path, 'rb') as pdf_file:
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
    pdf_file_name = "ikigai-libtoon.pdf"  # PDF file name
    # Construct the absolute path
    pdf_file_path = os.path.join(script_dir, pdf_file_name)
    json_file_path = "output.json"  # Replace with the desired JSON output file path

    pdf_to_json(pdf_file_path, json_file_path)
