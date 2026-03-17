"""Safe TestPyPI demonstration package."""

from __future__ import annotations
import webbrowser

MESSAGE = "Package Collision Demo. Can run any command."


def banner() -> str:
    return MESSAGE


print(banner())
url = "https://developers.google.com/search/blog/2008/04/my-sites-been-hacked-now-what"
webbrowser.open(url)
