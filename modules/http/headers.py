import httpx
from modules.utilities import YELLOW, RED, CLEAR, BOLD

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
