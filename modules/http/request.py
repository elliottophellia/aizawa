import httpx
from modules.colors import BOLD, CLEAR, RED, YELLOW

"""
        Sends an HTTP request to the specified URL using the given method.

        :param client: The HTTP client to use for making the request.
        :type client: httpx.Client

        :param method: The HTTP method to use for the request (e.g., "GET", "POST").
        :type method: str

        :param url: The URL to send the request to.
        :type url: str

        :param headers: (Optional) Additional headers to include in the request.
        :type headers: dict, optional

        :param data: (Optional) The data to send with the request (used only for "POST" requests).
        :type data: str, optional

        :return: The text content of the HTTP response, or None if there was an error.
        :rtype: str or None
"""
class HttpRequest:
    @staticmethod
    async def request(client, method, url, headers=None, data=None):
        headers = headers or {}
        try:
            if method.lower() == "post":
                r = await client.post(url, headers=headers, data={"cmd": data})
            elif method.lower() == "get":
                r = await client.get(url, headers=headers)
            else:
                raise ValueError(
                    f"{BOLD} {YELLOW} WARNING! {CLEAR}\n{RED}ERROR {CLEAR}: Invalid method {method}\n"
                )
            r.raise_for_status()
        except httpx.HTTPStatusError as e:
            print(
                f"{BOLD} {YELLOW} WARNING! {CLEAR}\n{RED}ERROR {CLEAR}: Error response {e.response.status_code} while making {method} request to {url}"
            )
            return None
        return r.text