# Import the necessary modules
import PyPDF2
import argparse
import os

# Create the argument parser
parser = argparse.ArgumentParser(description="Split a PDF file into smaller PDF files")
# Add an argument for the original file name
parser.add_argument("file", help="The name of the original PDF file (example: mybook.pdf)")
# Add an optional argument for the number of pages or the range of pages in each file
parser.add_argument("-p", "--pages", help="The number of pages in each file or Extract specific range in one file (example: 10 or 10_50)", default="1")
# Parse the arguments passed to the script
args = parser.parse_args()

# Open the original file for reading
source_pdf = open(args.file, "rb")
pdf_reader = PyPDF2.PdfReader(source_pdf)

# Get the number of pages in the original file
total_pages = len(pdf_reader.pages)

# Determine the base name and the extension of the original file
base_name, ext = os.path.splitext(os.path.basename(args.file))

# Create a folder with the base name to save the resulting files
output_dir = base_name
if not os.path.exists(output_dir): 
    os.mkdir(output_dir) 

# Check the type of the pages argument
if "_" in args.pages:
    # If the argument contains an underscore, it means it represents a range of pages
    # Convert the argument to a list of numbers
    pages_range = list(map(int, args.pages.split("_")))
    # Validate the range of pages
    if len(pages_range) != 2 or pages_range[0] < 1 or pages_range[1] > total_pages or pages_range[0] > pages_range[1]:
        print("Error: Invalid range of pages")
        exit()
    # Create a PdfFileWriter object to write the selected pages
    pdf_writer = PyPDF2.PdfFileWriter()
    # Loop over the selected pages and add them to the object
    for i in range(pages_range[0] - 1, pages_range[1]):
        pdf_writer.addPage(pdf_reader.getPage(i))
    # Determine the name of the resulting file
    file_name = f"{pages_range[0]}-{pages_range[1]}.pdf"
    # Determine the target path for the resulting file
    target_path = os.path.join(output_dir, file_name)
    # Open the resulting file for writing
    target_pdf = open(target_path, "wb")
    # Write the selected pages to the resulting file
    pdf_writer.write(target_pdf)
    # Close the resulting file
    target_pdf.close()
    # Print a success message
    print(f"Extracted pages from {pages_range[0]} to {pages_range[1]} from {args.file} and saved them in {target_path}")
else:
    # If the argument does not contain an underscore, it means it represents the number of pages in each file
    # Convert the argument to an integer
    pages_per_file = int(args.pages)
    # Validate the number of pages
    if pages_per_file < 1 or pages_per_file > total_pages:
        print("Error: Invalid number of pages")
        exit()
    # Calculate the number of resulting files
    num_files = (total_pages + pages_per_file - 1) // pages_per_file
    # Loop over the number of resulting files
    for i in range(num_files):
        # Create a PdfFileWriter object to write the pages in each file
        pdf_writer = PyPDF2.PdfWriter()
        # Calculate the first and the last page number in each file
        start_page = i * pages_per_file
        end_page = min((i + 1) * pages_per_file, total_pages)
        # Loop over the pages in each file and add them to the object
        for j in range(start_page, end_page):
            pdf_writer.add_page(pdf_reader.pages[j])
        # Determine the name of the resulting file
        file_name = f"{start_page + 1}-{end_page}.pdf"
        # Determine the target path for the resulting file
        target_path = os.path.join(output_dir, file_name)
        # Open the resulting file for writing
        target_pdf = open(target_path, "wb")
        # Write the pages in each file to the resulting file
        pdf_writer.write(target_pdf)
        # Close the resulting file
        target_pdf.close()
        # Print a success message
        print(f"Split pages from {start_page + 1} to {end_page} from {args.file} and saved them in {target_path}")
# Close the original file
source_pdf.close()
