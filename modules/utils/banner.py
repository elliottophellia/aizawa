from .colors import *

def banner():
    banner_text = YELLOW + "\n   ___   ________  ___ _      _____ \n"
    banner_text += "  / _ | /  _/_  / / _ | | /| / / _ |\n"
    banner_text += " / __ |_/ /  / /_" + BLUE + "/ __ | |/ |/ / __ |\n"
    banner_text += "/_/ |_/___/ /___/_/ |_|__/|__/_/ |_|" + CLEAR + "\n"
    banner_text += "A Super Simple Command Line Webshell\nFor Bypassing Any Kind of WAF or IDS\n"
    banner_text += "Code by " + BOLD + "   @" + RED + "elliottophellia" + CLEAR + "    "
    banner_text += BOLD + "#" + RED + "V" + PURPLE + "S" + BLUE + "P" + YELLOW + "O" + CLEAR + "\n"
    print(banner_text)