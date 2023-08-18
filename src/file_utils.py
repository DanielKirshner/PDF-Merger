import os


@staticmethod
def is_file(file_path: str) -> bool:
    return os.path.isfile(file_path)


@staticmethod
def is_file_pdf(file_path: str) -> bool:
    return file_path.endswith(".pdf")
