from PyPDF2 import PdfMerger

class PdfMergerHandler:
    
    def __enter__(self):
        PDF_MERGER_THROW_EXCEPTIONS = False
        self.merger_handle = PdfMerger(strict=PDF_MERGER_THROW_EXCEPTIONS)
        return self


    def append_to_pdf(self, pdf_path_to_append: str):
        self.merger_handle.append(pdf_path_to_append)
    
    
    def write_to_pdf(self, pdf_output_path: str):
        self.merger_handle.write(pdf_output_path)
    
    
    def __exit__(self, exception_type, exception_value, traceback):
        self.merger_handle.close()
        