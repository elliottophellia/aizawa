
```bash
    ___   ________  ___ _      _____
   / _ | /  _/_  / / _ | | /| / / _ |
  / __ |_/ /  / /_/ __ | |/ |/ / __ |
 /_/ |_/___/ /___/_/ |_|__/|__/_/ |_|
```
# Aizawa
Aizawa is a command-line tools designed to execute commands through HTTP header, enabling it to circumvent Web Application Firewalls (WAF) and Intrusion Detection Systems (IDS). Additionally, it is capable of bypassing `disable_function` restrictions, making it a tool of interest for security researchers and penetration testers. The name "Aizawa" is derived from Aizawa Ema, a virtual YouTuber associated with the Virtual Esport Project (VSPO), a group known for its focus on esports and virtual content creation.

![Python](https://img.shields.io/badge/PYTHON-3.13+-bf616a?style=flat-square) ![License](https://img.shields.io/badge/LICENSE-GPL--3.0-ebcb8b?style=flat-square) ![Version](https://img.shields.io/badge/VERSION-3.0.0-a3be8c?style=flat-square) [<img src="https://api.gitsponsors.com/api/badge/img?id=574290720" height="20">](https://api.gitsponsors.com/api/badge/link?p=KFYbutSs0pvM3IDfCOxUy/k3GP0oy6rjbvn0jbTQXtJFoK301ViM2T8gDX7u8jufoUS2dProxfv9X49YMFEy1OlylREWQfiN5iRVgzC9t/EXFH2xObRnKkc15nef0PfCVZgaGNqlO9c4XS0z7kRUgj5JfTO5xlhj7JIpdcOWlDw=)

[![Buy Me a Coffee](https://img.shields.io/badge/BUY%20ME%20A%20COFFEE-79B8CA?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/ReidhoSatria) [![Traktir Saya Kopi](https://img.shields.io/badge/TRAKTIR%20SAYA%20KOPI-FAC76C?style=for-the-badge&logo=BuyMeACoffee&logoColor=black)](https://saweria.co/elliottophellia)

[![Changelogs](https://img.shields.io/badge/CHANGELOGS-2e3440?style=for-the-badge)](#Changelogs) [![Prerequisites](https://img.shields.io/badge/PREREQUISITES-2e3440?style=for-the-badge)](#Prerequisites) [![Installation](https://img.shields.io/badge/INSTALLATION-2e3440?style=for-the-badge)](#Installation) [![Features](https://img.shields.io/badge/FEATURES-2e3440?style=for-the-badge)](#Screenshot) [![License](https://img.shields.io/badge/LICENCE-2e3440?style=for-the-badge)](#Licence) [![Disclaimer](https://img.shields.io/badge/DISCLAIMER-2e3440?style=for-the-badge)](#Disclaimer)

> [!WARNING]
> The tools is optimally compatible with PHP versions below 8.2. Users may experience connectivity issues when attempting to use this tool with PHP environments running version 8.2 or higher. This is a known issue that is currently being addressed in future updates.

> [!IMPORTANT]
> The shell itself is moved to [aizawa-webshell](https://github.com/elliottophellia/aizawa-webshell) repository. This repository is now dedicated to the client.

## Changelogs

### Major Changes

#### Security Enhancements
- Improved XOR encryption with random IV (initialization vector) per message
- Enhanced protection against pattern analysis and replay attacks
- Maintains backward compatibility with PHP 5.3 - 8.1

#### Infrastructure Overhaul
- Migrated from Poetry to uv for faster, more reliable dependency management
- Restructured to professional src-layout (`src/aizawa/`) for better package distribution
- Updated build system to use hatchling backend

#### Python Modernization
- Upgraded to Python 3.13+ with modern language features
- Implemented `from __future__ import annotations` throughout codebase
- Adopted PEP 585 type hints (`type[...]` instead of `Type[...]`)
- Utilized `Self` type hint (PEP 673) for better type inference
- Converted terminal colors to `StrEnum` (PEP 663) for type safety
- Added `TYPE_CHECKING` blocks for optimized runtime imports

#### Code Quality & Type Safety
- Achieved 100% type coverage with mypy strict mode (0 errors)
- Configured ruff with comprehensive ruleset (all checks enabled)
- Added complete Google-style docstrings for all public APIs
- Reorganized code into logical modules (core, http, utils)
- Enhanced error messages with better formatting and clarity

#### API Improvements
- Renamed classes for better clarity:
  - `Executor` → `CommandExecutor`
  - `Validator` → `InputValidator`
  - `HttpClient` → `AsyncHttpClient`
  - `display_banner()` → `render_banner()`
  - `Colors` → `TerminalColors`
- Updated httpx client to use modern `proxy` parameter (was `proxies`)
- Improved type hints on all public methods and functions

#### License Change
- Changed from CC-BY-SA-4.0 to GNU GPL-3.0-or-later
- Provides better protection for open-source contributions
- Ensures derivative works remain free and open

## Prerequisites

- Python 3.13+
- uv
- httpx
- validators

## Installation

### Release
```bash
# Install using pip
pip install aizawa
```

### Development
```bash
# Clone the repository
git clone https://github.com/elliottophellia/aizawa

# Change directory
cd aizawa

# Install dependencies using uv
uv sync

# Build the package
uv build

# Install the package
pip install dist/aizawa-3.0.0-py3-none-any.whl
```

## Usage

```bash
# Basic usage
aizawa --help

# With arguments
aizawa -u <URL> -k <KEY>

# With proxy
aizawa -u <URL> -k <KEY> -p <PROXY_URL>
```

### Command Line Arguments

- `-u, --url`: tools URL
- `-k, --key`: tools encryption key
- `-p, --proxy`: Proxy URL (e.g., http://127.0.0.1:8080)
- `-v, --version`: Show version information

## Features

- XOR encrypted command transmission
- Proxy support
- Async HTTP requests
- Multiple execution methods
- Enhanced error handling
- WAF/IDS evasion
- disable_function bypass
- Secure communication protocol

## License

This project is licensed under the GNU General Public License v3.0 or later (GPL-3.0-or-later). For more information, please refer to the [LICENSE](LICENSE) file included in this repository.

## Disclaimer

This project is intended solely for educational and research purposes. The author does not endorse, condone, or encourage any unauthorized or illegal use of this tool. Users are solely responsible for ensuring that their actions comply with all applicable laws and regulations. The author shall not be held liable for any misuse, damage, or consequences arising from the use of this software.
