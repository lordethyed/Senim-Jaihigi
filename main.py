import pdfplumber
from pathlib import Path

def pdf_to_mp3(file_path='test.pdf', language='en'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':

        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        text = ''.join(pages)

        with open('textl.txt', 'w') as file:
            file.write(text)

        text = text.replace('\n', '')

        with open('textl.txt', 'w') as file:
            file.write(text)
    else:
        return "File not exists, check the file paht!"

def main():
    print(pdf_to_mp3(file_path='/home/olzhas/Desktop/pet.pdf'))

if __name__ == '__main__':
    main()