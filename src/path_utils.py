import os

@staticmethod
def combine_full_path(directory: str, file_name: str) -> str:
    return os.path.join(os.getcwd(), directory, file_name)