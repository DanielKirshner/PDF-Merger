import os

@staticmethod
def combine_full_path(path: str) -> str:
    return os.path.join(os.getcwd(), path)