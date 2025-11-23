"""Display utilities for banner and visual output."""

from __future__ import annotations

from aizawa.utils.terminal import TerminalColors


def render_banner() -> None:
    """Display the application banner with styled ASCII art."""
    author = f"{TerminalColors.BOLD}@{TerminalColors.RED}elliottophellia"
    banner_text = f"""{TerminalColors.YELLOW}
    ___   ________  ___ _      _____
   / _ | /  _/_  / / _ | | /| / / _ |
  / __ |_/ /  / /_{TerminalColors.BLUE}/ __ | |/ |/ / __ |
 /_/ |_/___/ /___/_/ |_|__/|__/_/ |_|{TerminalColors.CLEAR}
The Ninja's Choice for Web Operations
      Code by {author}{TerminalColors.CLEAR}
"""
    print(banner_text)
