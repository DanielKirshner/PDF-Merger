import os


@staticmethod
def combine_full_path(file_name: str, directory: str=None) -> str:
    if directory == None:
        return os.path.join(os.getcwd(), file_name)
    return os.path.join(os.getcwd(), directory, file_name)

@staticmethod
def path_exists(full_path: str) -> bool:
    return os.path.exists(full_path)
