from pretty_errors_handle import PrettyErrorsHandle
from PyPDF2 import PdfMerger
from rich import print

import merge_logic


def main():
    p_errors_handle = PrettyErrorsHandle()
    merge_logic.run_logic()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("[bold red]Stopped.")
    except Exception as unhandled_exception:
        print("[bold red]Unhandled exception caught.")