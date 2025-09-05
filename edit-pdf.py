import os
from os import listdir
from os.path import isfile, join
import sys
import csv
import pymupdf

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
    output_path = os.path.join(folder_path, "edited")
    if not os.path.isdir(output_path):
        os.mkdir(output_path)
    for filename in [f for f in listdir(folder_path) if isfile(join(folder_path, f)) and f != 'desktop.ini']:
        print("Processing: " + filename)
        filename_base = os.path.splitext(filename)[0]
        output_filename = os.path.join(output_path, filename_base + ".edited.pdf")
        doc = pymupdf.open(os.path.join(folder_path, filename))
       
        page_number = 0
        for page in doc:
            print("Page " + str(page_number + 1) + "...")

            for s in substitution_dict.items():
                text_instances = page.search_for(s[0])
                # Redact each instance found, increasing the textbox size
                for inst in text_instances:
                    inst.y0 = inst.y0 - 2
                    inst.y1 = inst.y1 + 2
                    inst.x0 = inst.x0 + 2
                    inst.x1 = inst.x1 + 2
                    page.add_redact_annot(inst, text=s[1], fontsize=11)
            # Apply the redactions and insert the new text
            page.apply_redactions()

            page_number += 1
        doc.save(output_filename)
        print("Wrote: " + output_filename)


def check_input_folder(folder_path):
    """ Check that the input folder path is given and that it exists """
    if not os.path.isdir(folder_path):
        print("Input PDF path %s is not a folder!" % folder_path)
        exit()
    return folder_path

if __name__ == "__main__":
    main()