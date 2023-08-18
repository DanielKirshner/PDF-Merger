from PyPDF2 import PdfMerger

from path_input import *
from path_utils import *


OUTPUT_DIRECTORY_NAME = "out"
PDF_MERGER_THROW_EXCEPTIONS = False
OUTPUT_FILE_SHOULD_EXISTS = False


@staticmethod
def run_logic() -> None:
    pdf_paths = get_list_of_paths_from_user()
    
    if not path_exists(combine_full_path(OUTPUT_DIRECTORY_NAME)):
        os.makedirs(combine_full_path(OUTPUT_DIRECTORY_NAME))
    
    print("[cyan]Enter output pdf file name:")
    output_file_name_from_user = get_path_from_user(OUTPUT_FILE_SHOULD_EXISTS)
    full_output_merged_pdf_path = combine_full_path(output_file_name_from_user, OUTPUT_DIRECTORY_NAME)
    merger = PdfMerger(strict=PDF_MERGER_THROW_EXCEPTIONS)
    
    for current_pdf in pdf_paths:
        print(f"Appending {current_pdf} to {full_output_merged_pdf_path}")
        merger.append(current_pdf)
        
    merger.write(full_output_merged_pdf_path)
    print(f"[green]All files merged into {full_output_merged_pdf_path}")
    
    merger.close()
