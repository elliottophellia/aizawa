from aizawa.utils.colors import Colors

def display_banner() -> None:
    banner = f"""{Colors.YELLOW}
    ___   ________  ___ _      _____
   / _ | /  _/_  / / _ | | /| / / _ |
  / __ |_/ /  / /_{Colors.BLUE}/ __ | |/ |/ / __ |
 /_/ |_/___/ /___/_/ |_|__/|__/_/ |_|{Colors.CLEAR}
The Ninja's Choice for Web Operations
      Code by {Colors.BOLD}@{Colors.RED}elliottophellia{Colors.CLEAR}
"""
    print(banner)
