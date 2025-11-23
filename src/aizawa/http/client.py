"""Async HTTP client for web operations."""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING, Any, Self

import httpx

from aizawa.http.headers import generate_request_headers
from aizawa.utils.terminal import TerminalColors

if TYPE_CHECKING:
    import types
    from collections.abc import Mapping


class AsyncHttpClient:
    """Asynchronous HTTP client with proxy support and error handling."""

    def __init__(self, *, proxy_url: str | None = None) -> None:
        """Initialize the async HTTP client.

        Args:
            proxy_url: Optional proxy URL for HTTP/HTTPS requests.

        """
        self._client = httpx.AsyncClient(
            verify=False,
            timeout=None,
            proxy=proxy_url,
        )

    async def __aenter__(self) -> Self:
        """Enter async context manager."""
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: types.TracebackType | None,
    ) -> None:
        """Exit async context manager and cleanup resources."""
        await self._client.aclose()

    async def send_request(
        self,
        method: str,
        url: str,
        *,
        headers: Mapping[str, str] | None = None,
        data: Mapping[str, Any] | None = None,
    ) -> str | None:
        """Send HTTP request and return response text.

        Args:
            method: HTTP method (GET, POST, etc.).
            url: Target URL for the request.
            headers: Optional custom headers.
            data: Optional request data.

        Returns:
            Response text if successful, None otherwise.

        """
        request_headers = headers or generate_request_headers()
        try:
            response = await self._client.request(
                method,
                url,
                headers=request_headers,
                data=data,
            )
            response.raise_for_status()
            return response.text
        except httpx.HTTPError as http_err:
            print(f"{TerminalColors.RED}HTTP Error: {http_err!s}{TerminalColors.CLEAR}")
            return None
        except Exception as err:
            print(f"{TerminalColors.RED}Error: {err!s}{TerminalColors.CLEAR}")
            return None

    async def check_connectivity(self, url: str) -> None:
        """Verify connectivity to target URL.

        Args:
            url: Target URL to test connectivity.

        Raises:
            SystemExit: If unable to connect to the target.

        """
        if await self.send_request("GET", url) is None:
            sys.exit(
                print(
                    f"{TerminalColors.BOLD}{TerminalColors.YELLOW}"
                    f"WARNING!{TerminalColors.CLEAR}\n"
                    f"{TerminalColors.RED}ERROR{TerminalColors.CLEAR}: "
                    "Unable to connect to the shell\n"
                    "Please check the URL and try again\n",
                ),
            )

    async def fetch_headers(self, url: str) -> Mapping[str, str] | None:
        """Fetch HTTP headers from target URL.

        Args:
            url: Target URL to fetch headers from.

        Returns:
            Response headers if successful, None otherwise.

        """
        response = await self._client.head(url)
        return response.headers
