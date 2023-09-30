from PyPDF2 import PdfReader, PdfWriter


@staticmethod
def run_logic() -> None:
    page_indexes = [1, 2]
    
    with open("./out/merged.pdf", "rb") as f:
        reader = PdfReader(f)
        first_writer = PdfWriter()
        second_writer = PdfWriter() # the rest pages
        
        for page_index in range(len(reader.pages)):
            if page_index in page_indexes:
                first_writer.add_page(reader.pages[page_index])
            else:
                second_writer.add_page(reader.pages[page_index])
        
        with open("./out/selected.pdf", "wb") as f2:
            first_writer.write(f2)
            
        with open("./out/rest.pdf", "wb") as f2:
            second_writer.write(f2)
            
run_logic()

