from PyPDF2 import PdfMerger
import merge_logic

PDF_PATHS: list[str] = [".\\tests\\first.pdf", ".\\tests\\second.pdf", ".\\tests\\third.pdf"]
OUTPUT_PDF_PATH: str = ".\\tests\\merged.pdf"

def main():
    merge_logic.run_logic(PDF_PATHS, OUTPUT_PDF_PATH)

if __name__ == "__main__":
    main()
