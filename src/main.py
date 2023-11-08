from pretty_errors_handle import PrettyErrorsHandle
from rich import print
import merge_logic


def main():
    PrettyErrorsHandle()
    merge_logic.run_logic()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("[bold red]Stopped.")
    except IOError:
        print("[bold red]Input/Output exception caught.")
    except Exception:
        print("[bold red]Unhandled exception caught.")
