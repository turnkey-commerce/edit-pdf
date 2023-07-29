# Edit PDF

A Python program for making small edits in a PDF file by substituting certain text strings with a given substitition string. Rather than modifying the original PDF file it will create a new file with the replaced text.

One or more PDF files can be processed in batch by placing them in a given directory and specifying the directory to process.

Applications:

* Hide parts of an account number of a bank statement by substituting asterisks before sending to third parties.

* Fix incorrect addresses or other information.

* Redact sensitive information from a document.

## Install

 1. Install Python 3.
 2. Clone the EditPDF repository.
 3. In the EditPDF directory create a virtual environment:

    ```cmd
    python -m venv env
    ```

 4. Activate the env:

    ```cmd
    .\env\Scripts\activate.bat
    ```

 5. Install the requirements:

    ```cmd
    pip install -r requirements.txt
    ```

## Usage

 1. Edit the *substitutions.csv* file to have a comma-delimted list of the strings to be substituted in the first column and the substition string the second column, e.g.

    ```text
    6364625, *******
    Girard, Girardo
    ```

 2. Run the program with an argument to specify the folder of PDFs to process:

    ```cmd
    python edit-pdf.py pdfs
    ```

## License

MIT

See LICENSE file for more information.