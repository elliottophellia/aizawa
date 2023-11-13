import httpx
from modules.colors import YELLOW, RED, CLEAR, BOLD

"""
        Asynchronously sends a HEAD request to the specified URL using the provided client and returns the headers of the response.

        :param client: The HTTP client to use for sending the request.
        :type client: httpx.AsyncClient

        :param url: The URL to send the request to.
        :type url: str

        :return: The headers of the response, or None if an error occurred.
        :rtype: dict or None
"""
class GetHeaders:
    @staticmethod
    async def get_headers(client, url):
        try:
            r = await client.head(url)
            return r.headers
        except httpx.HTTPStatusError as e:
            print(
                f"{BOLD} {YELLOW} WARNING! {CLEAR}\n{RED}ERROR {CLEAR}: Error response {e.response.status_code} while making HEAD request to {url}"
            )
            return None
