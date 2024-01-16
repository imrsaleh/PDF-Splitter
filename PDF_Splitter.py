import PyPDF2
import sys

file_name = sys.argv[1]
pages_per_file = int(sys.argv[2])

source_pdf = open(file_name, "rb")
pdf_reader = PyPDF2.PdfFileReader(source_pdf)

total_pages = pdf_reader.getNumPages()

num_files = (total_pages + pages_per_file - 1) // pages_per_file

for i in range(num_files):
    pdf_writer = PyPDF2.PdfFileWriter()

    start_page = i * pages_per_file
    end_page = min((i + 1) * pages_per_file, total_pages)

    for j in range(start_page, end_page):
        pdf_writer.addPage(pdf_reader.getPage(j))

    target_pdf = open(f"file{i + 1}.pdf", "wb")

    pdf_writer.write(target_pdf)

    target_pdf.close()

source_pdf.close()
