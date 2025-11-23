"""Input validation and verification utilities."""

from __future__ import annotations

import re
import sys
from typing import TYPE_CHECKING

import validators

from aizawa.core.executor import CommandExecutor
from aizawa.utils.terminal import TerminalColors

if TYPE_CHECKING:
    from collections.abc import Mapping

    from aizawa.http.client import AsyncHttpClient


class InputValidator:
    """Validate user inputs and shell configurations."""

    VALID_SHELL_TYPES: frozenset[str] = frozenset({
        "http_aizawa_ninja_eval",
        "http_aizawa_ninja_concat",
        "http_aizawa_ninja_debug",
        "http_aizawa_ninja_gc",
        "http_aizawa_ninja_json",
        "http_aizawa_ninja_filter",
    })

    @staticmethod
    async def verify_encryption_key(
        client: AsyncHttpClient,
        url: str,
        shell_type: str,
        key: str,
    ) -> bool:
        """Verify that the encryption key is valid.

        Args:
            client: HTTP client for requests.
            url: Target shell URL.
            shell_type: Type of shell endpoint.
            key: Encryption key to verify.

        Returns:
            True if key is valid, False otherwise.

        """
        try:
            test_result = await CommandExecutor.run_command(
                client, url, "echo aizawa", shell_type, key,
            )

            if test_result and "aizawa" in test_result:
                return True

            print(
                f"{TerminalColors.BOLD}{TerminalColors.YELLOW}"
                f"WARNING!{TerminalColors.CLEAR}\n"
                f"{TerminalColors.RED}ERROR{TerminalColors.CLEAR}: "
                "Invalid shell key\n"
                "Please check your key and try again\n",
            )
            return False
        except Exception as err:
            print(
                f"{TerminalColors.BOLD}{TerminalColors.YELLOW}"
                f"WARNING!{TerminalColors.CLEAR}\n"
                f"{TerminalColors.RED}ERROR{TerminalColors.CLEAR}: "
                "Failed to verify shell key\n"
                f"{err!s}\n",
            )
            return False

    @staticmethod
    def validate_target_url(url: str) -> str:
        """Validate URL format and accessibility.

        Args:
            url: URL to validate.

        Returns:
            Validated URL.

        Raises:
            SystemExit: If URL is invalid.

        """
        if not validators.url(url):
            sys.exit(
                print(
                    f"{TerminalColors.BOLD}{TerminalColors.YELLOW}"
                    f"WARNING!{TerminalColors.CLEAR}\n"
                    f"{TerminalColors.RED}ERROR{TerminalColors.CLEAR}: "
                    "Invalid URL\n"
                    "Please check the URL and try again\n",
                ),
            )
        return url

    @staticmethod
    def validate_response_headers(
        headers: Mapping[str, str] | None,
    ) -> str:
        """Validate that response headers contain shell type.

        Args:
            headers: HTTP response headers to validate.

        Returns:
            Shell type from headers.

        Raises:
            SystemExit: If headers are invalid or missing shell type.

        """
        if headers is None or "Aizawa-Type" not in headers:
            sys.exit(
                print(
                    f"{TerminalColors.BOLD}{TerminalColors.YELLOW}"
                    f"WARNING!{TerminalColors.CLEAR}\n"
                    f"{TerminalColors.RED}ERROR{TerminalColors.CLEAR}: "
                    "This does not appear to be a valid Aizawa shell\n"
                    "Please check the server configuration and try again\n",
                ),
            )
        return headers["Aizawa-Type"]

    @staticmethod
    def validate_shell_type(shell_type: str) -> str:
        """Validate that shell type is supported.

        Args:
            shell_type: Shell type identifier to validate.

        Returns:
            Validated shell type.

        Raises:
            SystemExit: If shell type is not supported.

        """
        if shell_type not in InputValidator.VALID_SHELL_TYPES:
            sys.exit(
                print(
                    f"{TerminalColors.BOLD}{TerminalColors.YELLOW}"
                    f"WARNING!{TerminalColors.CLEAR}\n"
                    f"{TerminalColors.RED}ERROR{TerminalColors.CLEAR}: "
                    "This does not appear to be a valid Aizawa shell\n"
                    "Please check the server configuration and try again\n",
                ),
            )
        return shell_type

    @staticmethod
    def sanitize_shell_info(
        username: str,
        hostname: str,
        working_dir: str,
    ) -> tuple[str, str, str]:
        """Sanitize and normalize shell information strings.

        Args:
            username: User name from remote shell.
            hostname: Hostname from remote shell.
            working_dir: Working directory from remote shell.

        Returns:
            Tuple of (username, hostname, working_dir) with defaults if needed.

        """
        error_indicator = f"{TerminalColors.RED}ERROR{TerminalColors.CLEAR}"

        sanitized_user = (
            "aizawaema"
            if not username or username == error_indicator
            else re.sub(r"\s+", "", username)
        )

        sanitized_host = (
            "virtualesport"
            if not hostname or hostname == error_indicator
            else re.sub(r"\s+", "", hostname)
        )

        sanitized_pwd = (
            "~/unknown/path"
            if not working_dir or working_dir == error_indicator
            else re.sub(r"\s+", "", working_dir)
        )

        return sanitized_user, sanitized_host, sanitized_pwd
