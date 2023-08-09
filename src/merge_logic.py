from PyPDF2 import PdfMerger

@staticmethod
def run_logic(pdf_paths: list[str], output_merged_pdf_path: str) -> None:
    """
    Run merging logic

    Args:
        pdf_paths (list[str]): A list of all pdf paths to be merged
        output_merged_pdf_path (str): Output pdf file path (will created)
    """
    PDF_MERGER_THROW_EXCEPTIONS = False     # But it will log a warning message.
    merger = PdfMerger(strict=PDF_MERGER_THROW_EXCEPTIONS)
    
    for current_pdf in pdf_paths:
        print(f"Appending {current_pdf} to {output_merged_pdf_path}")
        merger.append(current_pdf)
        
    merger.write(output_merged_pdf_path)
    print(f"All files merged into {output_merged_pdf_path}")
    
    merger.close()
    # print(f"File descriptors closed and memory usage cleaned up.")
