from PyPDF2 import PdfMerger

PDF_FILES: list[str] = ["tests\\first.pdf", "tests\\second.pdf", "tests\\third.pdf"]

def logic():
    merger = PdfMerger()
    
    for pdf in PDF_FILES:
        merger.append(pdf)
        
    merger.write("tests\\merged.pdf")
    merger.close()

def main():
    logic()

if __name__ == "__main__":
    main()
