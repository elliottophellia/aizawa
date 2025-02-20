import sys
import re
from typing import Tuple, Dict, Optional
import validators
from aizawa.utils.colors import Colors
from aizawa.http.client import HttpClient
from aizawa.core.executor import Executor

class Validator:
    @staticmethod
    async def validate_key(client: HttpClient, url: str, shell_type: str, key: str) -> bool:
        try:
            test_result = await Executor.execute(client, url, "echo aizawa", shell_type, key)

            if test_result and "aizawa" in test_result:
                return True

            print(f"{Colors.BOLD}{Colors.YELLOW}WARNING!{Colors.CLEAR}\n{Colors.RED}ERROR{Colors.CLEAR}: Invalid webshell key\nPlease check your key and try again\n")
            return False
        except Exception as e:
            print(f"{Colors.BOLD}{Colors.YELLOW}WARNING!{Colors.CLEAR}\n{Colors.RED}ERROR{Colors.CLEAR}: Failed to verify webshell key\n{str(e)}\n")
            return False

    @staticmethod
    def validate_url(url: str) -> str:
        if not validators.url(url):
            sys.exit(
                print(
                    f"{Colors.BOLD}{Colors.YELLOW}WARNING!{Colors.CLEAR}\n{Colors.RED}ERROR{Colors.CLEAR}: Invalid URL\nPlease check the URL and try again\n"
                )
            )
        return url

    @staticmethod
    def validate_headers(headers: Optional[Dict[str, str]]) -> str:
        if headers is None or "Aizawa-Type" not in headers:
            sys.exit(
                print(f"{Colors.BOLD}{Colors.YELLOW}WARNING!{Colors.CLEAR}\n{Colors.RED}ERROR{Colors.CLEAR}: This not appear to be a valid Aizawa Webshell\nPlease check the server configuration and try again\n")
            )
        return headers["Aizawa-Type"]

    @staticmethod
    def validate_type(shell_type: str) -> str:
        valid_types = [
            "http_aizawa_ninja_eval",
            "http_aizawa_ninja_concat",
            "http_aizawa_ninja_debug",
            "http_aizawa_ninja_gc",
            "http_aizawa_ninja_json",
            "http_aizawa_ninja_filter",
        ]

        if shell_type not in valid_types:
            sys.exit(
                print(f"{Colors.BOLD}{Colors.YELLOW}WARNING!{Colors.CLEAR}\n{Colors.RED}ERROR{Colors.CLEAR}: This not appear to be a valid Aizawa Webshell\nPlease check the server configuration and try again\n")
            )
        return shell_type

    @staticmethod
    def process_user_host_pwd(user: str, host: str, pwd: str) -> Tuple[str, str, str]:
        user = "aizawaema" if not user or user == f"{Colors.RED}ERROR{Colors.CLEAR}" else re.sub(r"\s+", "", user)
        host = "virtualesport" if not host or host == f"{Colors.RED}ERROR{Colors.CLEAR}" else re.sub(r"\s+", "", host)
        pwd = "~/unknown/path" if not pwd or pwd == f"{Colors.RED}ERROR{Colors.CLEAR}" else re.sub(r"\s+", "", pwd)
        return user, host, pwd
