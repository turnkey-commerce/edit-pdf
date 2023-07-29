import os
from os import listdir
from os.path import isfile, join
import sys
import csv
import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.generic import DecodedStreamObject, StreamObject
from PyPDF2 import filters

target_folder = "converted_files"
substitution_dict = {}

def replace(text):
    if isinstance(text, bytes):
        for s in substitution_dict.items():
            try:
                text = text.replace(s[0].encode(), s[1].encode())              
            except:
                print("Error")

    return text

class EncodedStreamObject(StreamObject):
    def __init__(self):
        self.decodedSelf = None

    def getData(self):
        if self.decodedSelf:
            return self.decodedSelf.getData()
        else:
            decoded = DecodedStreamObject()

            decoded._data = filters.decodeStreamData(self)
            decoded._data = replace(decoded._data)

            for key, value in list(self.items()):
                if not key in ("/Length", "/Filter", "/DecodeParms"):
                    decoded[key] = value
            self.decodedSelf = decoded
            return decoded._data
        
PyPDF2.generic.EncodedStreamObject = EncodedStreamObject

def main():
    # Get the folder from the first argument.
    if len(sys.argv) > 1:
        folder_path = check_input_folder(sys.argv[1])
    else:
        print("Please provide folder to process")
        exit()

    with open("substitutions.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            substitution_dict[row[0].strip()] = row[1].strip()

    edit_pdf_files(folder_path)

def edit_pdf_files(folder_path):
    for filename in [f for f in listdir(folder_path) if isfile(join(folder_path, f))]:
        filename_base = os.path.splitext(filename)[0]
        output_filename = os.path.join(folder_path, "results", filename_base + ".result.pdf")
        reader = PdfFileReader(os.path.join(folder_path, filename))
        writer = PdfFileWriter()
        number_of_pages = len(reader.pages)
        for page_number in range(number_of_pages):
            print(page_number)
            page = reader.getPage(page_number)
            page.mergePage(reader.getPage(page_number))     

            writer.addPage(page)
        
        with open(output_filename, 'wb') as out_file:
            writer.write(out_file)
            print("Wrote: " + output_filename)


def check_input_folder(folder_path):
    """ Check that the input folder path is given and that it exists """
    if not os.path.isdir(folder_path):
        print("Input PDF path %s is not a folder!" % folder_path)
        exit()
    return folder_path

if __name__ == "__main__":
    main()