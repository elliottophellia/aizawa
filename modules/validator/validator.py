import re
import sys
import validators
from modules.colors import BOLD, YELLOW, CLEAR, RED

class Validator:
    """
        Validates a given URL.

        Parameters:
            url (str): The URL to be validated.

        Returns:
            str: The validated URL.

        Raises:
            SystemExit: If the URL is invalid.
    """
    @staticmethod
    def validate_url(url):
        if not validators.url(url):
            sys.exit(
                print(
                    f"{BOLD}{YELLOW}WARNING!{CLEAR}\n{RED}ERROR{CLEAR}: Invalid URL\nPlease check the URL and try again\n"
                )
            )
        return url
    
    """
        Validates the headers of the request.

        Args:
            headers (dict): The headers of the request.

        Returns:
            str: The value of the 'Aizawa-Type' header.

        Raises:
            SystemExit: If the headers are None or if the 'Aizawa-Type' header is not present.
    """
    @staticmethod
    def validate_headers(headers):
        if headers is None or "Aizawa-Type" not in headers:
            sys.exit(
                print(f"{BOLD}{YELLOW}WARNING!{CLEAR}\n{RED}ERROR{CLEAR}: This not appear to be a valid Aizawa Webshell\nPlease check the server configuration and try again\n")
            )
        return headers["Aizawa-Type"]
    
    """
        Validates the type parameter against a list of expected types.
        
        Args:
            type (str): The type to be validated.
        
        Returns:
            str: The validated type.
        
        Raises:
            SystemExit: If the type is not in the expected types list.
    """
    @staticmethod
    def validate_type(type):
        expected_types = [
            "http_accept_language_get",
            "http_user_agent_get",
            "http_accept_language_post",
            "http_user_agent_post",
            "http_aizawa_ninja_eval",
            "http_aizawa_ninja_concat",
            "http_aizawa_ninja_debug",
            "http_aizawa_ninja_gc",
            "http_aizawa_ninja_json",
            "http_aizawa_ninja_filter",
        ]

        if type not in expected_types:
            sys.exit(
                print(f"{BOLD}{YELLOW}WARNING!{CLEAR}\n{RED}ERROR{CLEAR}: This not appear to be a valid Aizawa Webshell\nPlease check the server configuration and try again\n")
            )
        return type

    """
        Process the user, host, and path for the given inputs.

        :param user: The username to process.
        :type user: str
        :param host: The hostname to process.
        :type host: str
        :param pwd: The path to process.
        :type pwd: str
        :return: A tuple containing the processed user, host, and path.
        :rtype: tuple
    """
    @staticmethod
    def process_user_host_pwd(user, host, pwd):
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
        return user, host, pwd