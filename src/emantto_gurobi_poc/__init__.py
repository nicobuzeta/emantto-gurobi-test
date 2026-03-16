"""Safe TestPyPI demonstration package."""

MESSAGE = "INJECTED DEMO: TestPyPI package selected"


def banner() -> str:
    return MESSAGE


def main() -> int:
    print(banner())
    return 0

