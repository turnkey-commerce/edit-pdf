# edit-pdf

edit-pdf is a simple Python program for making global edits in a PDF file by globally replacing text strings to a given substitition string. Rather than modifying the original PDF file it will create a new file with the replaced text.

One or more PDF files can be processed in batch by placing them in a given folder and specifying the folder to process.

Applications:

* Hide parts of an account number of a bank statement by substituting asterisks (*) before sending to third parties.

* Fix incorrect addresses or other information.

* Redact sensitive information from a document by replacing with asterisks (*).

## Install

 1. Install Python 3 if not already installed:

    ```cmd
    https://www.python.org/downloads/
    ```

 2. Clone the edit-pdf repository:

    ```cmd
    git clone https://github.com/turnkey-commerce/edit-pdf.git
    ```

 3. In the edit-pdf directory create a virtual environment:

    ```cmd
    python -m venv env
    ```

 4. Activate the env by running the appropriate script in the Scripts folder:

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

 2. Run the program with an argument to specify the folder containing the PDFs to process:

    ```cmd
    python edit-pdf.py folder
    ```

 3. The program will output a new version of each of the files to a subfolder called "edited". The edited files will also have ".edited" string added to the filename in front of the pdf extension, e.g. "filename.*edited*.pdf"

## License

MIT

See LICENSE file for more information.
