@staticmethod
def get_path_from_user() -> str:
    path = ''
    path_valid = False
    
    while not path_valid:
        print("Enter path -> ")
        path = str(input())
        
        if not isinstance(path, str) or len(path) == 0:
            print("Invalid path given.")
        else:
            path_valid = True
    
    return path


@staticmethod
def get_list_of_paths_from_user(num_of_paths: int) -> list[str]:
    paths = []
    for i in range(num_of_paths):
        paths.append(get_path_from_user())
    
    return paths
