from rich import print

@staticmethod
def get_path_from_user() -> str:
    path = ''
    path_valid = False
    
    while not path_valid:
        print("[cyan]Enter path -> ")
        path = str(input())
        
        if not isinstance(path, str) or len(path) == 0:
            print("[bold red]Invalid path given.")
        else:
            path_valid = True
    
    return path


@staticmethod
def get_list_of_paths_from_user() -> list[str]:
    num_of_paths = num_of_pdf_files_input()
    print(f"[purple]Enter {num_of_paths} paths:")
    
    paths = []
    for i in range(num_of_paths):
        paths.append(get_path_from_user())
    
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
