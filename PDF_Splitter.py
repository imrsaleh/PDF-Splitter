import PyPDF2
import sys
import os 

file_name = sys.argv[1]
pages_per_file = int(sys.argv[2])

source_pdf = open(file_name, "rb")
pdf_reader = PyPDF2.PdfFileReader(source_pdf)

total_pages = pdf_reader.getNumPages()

num_files = (total_pages + pages_per_file - 1) // pages_per_file

base_name = os.path.splitext(os.path.basename(file_name))[0]

output_dir = base_name
if not os.path.exists(output_dir): 
    os.mkdir(output_dir) 

for i in range(num_files):
    pdf_writer = PyPDF2.PdfFileWriter()

    start_page = i * pages_per_file
    end_page = min((i + 1) * pages_per_file, total_pages)

    for j in range(start_page, end_page):
        pdf_writer.addPage(pdf_reader.getPage(j))

    file_name = f"{start_page + 1}-{end_page}.pdf"

    target_path = os.path.join(output_dir, file_name)

    target_pdf = open(target_path, "wb")

    pdf_writer.write(target_pdf)

    target_pdf.close()

source_pdf.close()
