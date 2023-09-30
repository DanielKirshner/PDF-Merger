from PyPDF2 import PdfFileReader, PdfFileWriter


@staticmethod
def run_logic() -> None:
    page_indexes = [1, 2]
    
    with open("./out/merged.pdf", "rb") as f:
        reader = PdfFileReader(f)
        first_writer = PdfFileWriter()
        second_writer = PdfFileWriter() # the rest pages
        
        for page_index in range(len(reader.pages)):
            if page_index in page_indexes:
                first_writer.addPage(reader.getPage(page_index))
            else:
                second_writer.addPage(reader.getPage(page_index))
        
        with open("./out/selected.pdf", "wb") as f2:
            first_writer.write(f2)
            
        with open("./out/rest.pdf", "wb") as f2:
            second_writer.write(f2)
            
run_logic()

