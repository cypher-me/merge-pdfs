'''
    python script to merge multiple pdf files into one
    author: https://github.com/cypher-me
    remarks: Please mention me if you use this script(recommended not a must)
'''
import PyPDF2
import os

def merge_pdfs(pdf_dir, output_path):
    pdf_writer = PyPDF2.PdfWriter()

    for filename in os.listdir(pdf_dir):
        if filename.endswith('.pdf'):
            path = os.path.join(pdf_dir, filename)
            try:
                pdf_reader = PyPDF2.PdfReader(path)
                for page in pdf_reader.pages:
                    pdf_writer.add_page(page)
            except PyPDF2.utils.PdfReadError:
                print(f"Error reading file: {filename}")

    with open(output_path, 'wb') as output_file:
        pdf_writer.write(output_file)

if __name__ == "__main__":
    # pdf_directory = The folders you want to merge
    pdf_directory = './b4'
    # output_pdf = The name of the merged pdf file
    output_pdf = './after/merged_file.pdf'
    merge_pdfs(pdf_directory, output_pdf)
