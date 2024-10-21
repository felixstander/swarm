from datetime import datetime


class Colors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    RED = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    GREY = "\033[90m"


def debug_print(debug: bool, *args: str) -> None:
    if not debug:
        return
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    messages = " ".join(map(str, args))

    print(f"{Colors.OKBLUE}{timestamp}{Colors.ENDC}{messages}\n")

    print(f"{Colors.GREY}{timestamp}: {messages}{Colors.ENDC}")

    print(
        f"{Colors.HEADER}Expected function: {Colors.ENDC} {timestamp}, {Colors.HEADER}Got: {Colors.ENDC}{messages}\n"
    )
    print(f"{Colors.GREY}Selected engine: Assistants{Colors.ENDC}")


if __name__ == "__main__":
    messages = "hello"
    debug_print(True, messages, "world")
