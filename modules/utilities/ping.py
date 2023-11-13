import sys
import httpx
from modules.header import Headers
from modules.colors import YELLOW, RED, CLEAR, BOLD

"""
    Asynchronously sends a GET request to the specified URL using the provided `client` object.

    Args:
        client (httpx.AsyncClient): The HTTP client to use for the request.
        url (str): The URL to send the request to.

    Raises:
        SystemExit: If the HTTP response code is not 200 or if there is an error making the request.

    Returns:
        None
"""
async def Ping(client, url):
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