from .colors import YELLOW, BLUE, RED, CLEAR, BOLD, PURPLE
def Banner():
    banner_text = f"{YELLOW}\n   ___   ________  ___ _      _____ \n"
    banner_text += "  / _ | /  _/_  / / _ | | /| / / _ |\n"
    banner_text += f" / __ |_/ /  / /_{BLUE}/ __ | |/ |/ / __ |\n"
    banner_text += f"/_/ |_/___/ /___/_/ |_|__/|__/_/ |_|{CLEAR}\n"
    banner_text += "A Super Simple Command Line Webshell\nFor Bypassing Any Kind of WAF or IDS\n"
    banner_text += f"Code by {BOLD}   @{RED}elliottophellia{CLEAR}    "
    banner_text += f"{BOLD}#{RED}V{PURPLE}S{BLUE}P{YELLOW}O{CLEAR}\n"
    print(banner_text)