from PyPDF2 import PdfMerger

@staticmethod
def run_logic(pdf_paths: list[str], output_merged_pdf_path: str) -> None:
    
    GET_ALL_WARNINGS = True
    merger = PdfMerger(strict=GET_ALL_WARNINGS)
    
    for current_pdf in pdf_paths:
        merger.append(current_pdf)
        
    merger.write(output_merged_pdf_path)
    merger.close()
    