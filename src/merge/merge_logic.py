from PyPDF2 import PdfMerger

@staticmethod
def run_logic(pdf_paths: list[str]) -> None:
    
    GET_ALL_WARNINGS = True
    merger = PdfMerger(strict=GET_ALL_WARNINGS)
    
    for current_pdf in pdf_paths:
        merger.append(current_pdf)
        
    merger.write("tests\\merged.pdf")
    merger.close()
    