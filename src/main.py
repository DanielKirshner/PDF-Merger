from rich import print
from PyPDF2 import PdfMerger
import pretty_errors

import merge_logic


def main():
    merge_logic.run_logic()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("[bold red]Stopped.")
    except Exception as unhandled_exception:
        print("[bold red]Unhandled exception caught.")