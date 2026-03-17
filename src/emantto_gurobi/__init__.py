"""Safe TestPyPI demonstration package."""

from __future__ import annotations

MESSAGE = "Package Collision Demo. Can run any command."
POPUP_TITLE = "Demo Popup"


def banner() -> str:
    return MESSAGE


def show_popup(message: str) -> bool:
    """Show a best-effort desktop popup and report whether it succeeded."""
    try:
        import tkinter as tk
        from tkinter import messagebox

        root = tk.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        messagebox.showinfo(POPUP_TITLE, message, parent=root)
        root.destroy()
        return True
    except Exception:
        return False


def main() -> int:
    message = banner()
    popup_shown = show_popup(message)
    print(message)
    if not popup_shown:
        print("Popup could not be displayed in this environment.")
    return 0
