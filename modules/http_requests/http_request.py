import httpx
from modules.utils.colors import *

async def http_request(client, method, url, headers=None, data=None):
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