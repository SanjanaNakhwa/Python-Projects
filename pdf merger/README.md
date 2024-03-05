# PDF Merger

## Overview
This Python script allows you to merge multiple PDF files into a single PDF file. Simply provide the list of full paths to the PDF files you want to merge, and the script will handle the rest!

## Features
- Merge multiple PDF files into one.
- Utilizes the **PyPDF2** library for PDF manipulation.

## Requirements
- Python 3.x
- **PyPDF2** library

## Installation
1. Make sure you have Python 3.x installed on your system. If not, you can download it from the [official Python website](https://www.python.org/downloads/).
2. Install the **PyPDF2** library by running the following command:

```
pip install PyPDF2
```


## Usage
1. Open your terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Edit the script to specify the full paths to the PDF files you want to merge in the `pdf_files` list.
4. Run the script with the following command:

```
python pdf_merger.py
```


## Example

# List of full paths to the PDF files you want to merge

```
pdf_files = [
 "/Users/sanjananakhwa/Desktop/CS697/1. Intro_to_machine_learning.pdf",
 "/Users/sanjananakhwa/Desktop/CS697/65_jailbreaking_black_box_large_l.pdf"
]
```

## Output
The merged PDF file will be saved in the same directory as the input PDF files with the name "CombinedDoc.pdf".

## Disclaimer
Please ensure that you have the necessary permissions to merge and use the PDF files before running this script. Misuse or unauthorized merging of PDF files may violate copyright laws and regulations.
