import PyPDF2
import json
import os


def extract_transaction_data(pdf_file_path, password):
    transaction_data = []

    with open(pdf_file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        if pdf_reader.is_encrypted:
            pdf_reader.decrypt(password)

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()
            print(f"Page {page_num + 1} text: {page_text}")

            # Implement logic to extract and format data from the page_text
            # Append the formatted data to the transaction_data list

            # For example, you can split the page_text into lines and add each line to the list
            lines = page_text.split('\n')
            transaction_data.extend(lines)

    return transaction_data


if __name__ == "__main__":
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_file_name = "2023-09.pdf"  # PDF file name
    # Construct the absolute path
    pdf_file_path = os.path.join(script_dir, pdf_file_name)
    password = 'your_password_here'  # Replace with the actual password

    transaction_data = extract_transaction_data(pdf_file_path, password)

    # Convert the extracted data to JSON and write it to a file
    with open("output.json", 'w', encoding='utf-8') as json_file:
        json.dump({"pages": transaction_data}, json_file,
                  indent=4, ensure_ascii=False)
