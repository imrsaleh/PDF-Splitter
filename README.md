# PDF-Splitter
This is a simple project that uses the PyPDF2 library to split a PDF file into smaller PDF files based on the number of pages.

# Requirements
- Python 3.6 or higher

# install

Download PDF_Splitter.py file on your machine
- Open CMD and Install the PyPDF2 library using the following command:

```
pip install PyPDF2==2.1.0
```

# Usage
- Place the PDF file that you want to split in the same folder that contains the script
- Open CMD and put yourself in the same location. 

for help use this command
```
PDF_Splitter.py -h
```
if you want to Split a PDF pages into smaller PDF files use the following command: (example: 20 pages for each file )

```
python PDF_Splitter.py -p 20 book.pdf
```

if you want to Extract specific range in one file use the following command: (example: from page 50 to 100 )

```
python PDF_Splitter.py -p 50_100 book.pdf
```

- The script will generate split PDF files in the same folder and will be named according to the pages inside

# Contribution

If you have any suggestions or improvements for this project, feel free to create a pull request or an issue.



# License
This project is licensed under the MIT License. See the LICENSE file for more details.
