import sys
import httpx
from aizawa.utils.colors import Colors
from typing import Optional, Dict, Any
from aizawa.http.headers import create_headers

class HttpClient:
    def __init__(self, proxy: Optional[str] = None):
        proxies = {"http://": proxy, "https://": proxy} if proxy else None
        self.client = httpx.AsyncClient(
            verify=False,
            timeout=None,
            proxies=proxies
        )

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.client.aclose()

    async def request(self, method: str, url: str, headers: Optional[Dict[str, str]] = None, data: Optional[Dict[str, Any]] = None) -> Optional[str]:
        headers = headers or create_headers()
        try:
            response = await self.client.request(method, url, headers=headers, data=data)
            response.raise_for_status()
            return response.text
        except httpx.HTTPError as e:
            print(f"{Colors.RED}HTTP Error: {str(e)}{Colors.CLEAR}")
            return None
        except Exception as e:
            print(f"{Colors.RED}Error: {str(e)}{Colors.CLEAR}")
            return None

    async def ping(self, url: str) -> None:
        if  await self.request("GET", url) is None:
            sys.exit(
                print(
                    f"{Colors.BOLD}{Colors.YELLOW}WARNING!{Colors.CLEAR}\n{Colors.RED}ERROR{Colors.CLEAR}: Unable to connect to the webshell\nPlease check the URL and try again\n"
                )
            )

    async def get_headers(self, url: str) -> Optional[Dict[str, str]]:
        response = await self.client.head(url)
        return response.headers
