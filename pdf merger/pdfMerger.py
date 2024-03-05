import sys
import PyPDF2
import os

# Create a PdfMerger object
merger = PyPDF2.PdfMerger()

# List of full paths to the PDF files you want to merge
pdf_files = [
    "/Users/sanjananakhwa/Desktop/CS697/1. Intro_to_machine_learning.pdf",
    "/Users/sanjananakhwa/Desktop/CS697/65_jailbreaking_black_box_large_l.pdf"
]

# Append each PDF file to the merger
for file in pdf_files:
    merger.append(file)

# Get the directory path of the first input PDF file
output_dir = os.path.dirname(pdf_files[0])

# Create the full path for the output file
output_file_path = os.path.join(output_dir, "CombinedDoc.pdf")

# Write the merged PDF to the output file
with open(output_file_path, "wb") as output_file:
    merger.write(output_file)

# Close the merger
merger.close()