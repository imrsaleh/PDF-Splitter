# PDF-Splitter
This is a simple project that uses the PyPDF2 library to split a PDF file into smaller PDF files based on the number of pages.

Requirements
- Python 3.6 or higher

Usage:

Download PDF_Splitter.py file on your machine
- Open CMD and Install the PyPDF2 library using the following command:

```
pip install PyPDF2==2.1.0
```
- Place the PDF file that you want to split in the same folder that contains the script
- Open CMD put yourself in the same location and use the following command:
```
python PDF_Splitter.py book.pdf 20
```
1- book.pdf ( PDF file name )

2- number of pages per file ( 20 for example )

- The script will generate split PDF files in the same folder and will be named according to the pages inside

ContributionIf you have any suggestions or improvements for this project, feel free to create a pull request or an issue.



# License
This project is licensed under the MIT License. See the LICENSE file for more details.
