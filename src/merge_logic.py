from PyPDF2 import PdfMerger
from path_input import *


@staticmethod
def run_logic() -> None:
    pdf_paths = get_list_of_paths_from_user()
    print("[cyan]Enter output path:")
    OUTPUT_FILE_SHOULD_EXISTS = False
    output_merged_pdf_path = get_path_from_user(OUTPUT_FILE_SHOULD_EXISTS)
    
    PDF_MERGER_THROW_EXCEPTIONS = False
    merger = PdfMerger(strict=PDF_MERGER_THROW_EXCEPTIONS)
    
    for current_pdf in pdf_paths:
        print(f"Appending {current_pdf} to {output_merged_pdf_path}")
        merger.append(current_pdf)
        
    merger.write(output_merged_pdf_path)
    print(f"[green]All files merged into {output_merged_pdf_path}")
    
    merger.close()
