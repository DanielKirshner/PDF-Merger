from rich import print
import file_utils


@staticmethod
def get_path_from_user(file_should_exists: bool) -> str:
    path = ''
    path_valid = False
    
    while not path_valid:
        print("[cyan]Enter path -> ")
        path = str(input())
        
        if not isinstance(path, str) or len(path) == 0:
            print("[bold red]Invalid path given.")
            continue
        else:
            path_valid = True
            
        if file_should_exists:
            if not file_utils.is_file(path):
                print(f"[bold red]File {path} does not exists.")
                path_valid = False
                continue
            else:
                path_valid = True
            
            if not file_utils.is_file_pdf(path):
                print(f"[bold red]File {path} is not a PDF")
                path_valid = False
                continue
            else:
                path_valid = True
                
    return path


@staticmethod
def get_list_of_paths_from_user() -> list[str]:
    num_of_paths = num_of_pdf_files_input()
    print(f"[purple]Enter {num_of_paths} paths:")
    
    paths = []
    for i in range(num_of_paths):
        PDF_FILE_SHOULD_EXISTS = True
        paths.append(get_path_from_user(PDF_FILE_SHOULD_EXISTS))
    
    return paths


def num_of_pdf_files_input() -> int:
    print("[cyan]Enter amount of pdf files ->")
    num_of_pdf_files_input_str = str(input())
    
    valid_number = False
    number = 0
    while not valid_number:
        if num_of_pdf_files_input_str.isnumeric():
            number = int(num_of_pdf_files_input_str)
            if number != 0:
                valid_number = True
        
        if not valid_number:
            print("[bold red]Invalid amount input!\nTry again ->")
            num_of_pdf_files_input_str = str(input())
    return number
