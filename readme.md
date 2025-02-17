<p align='center'>
<img src='./images/aizawa.png' width='300'/><br/><img src="https://img.shields.io/badge/AIZAWA%20BYPASS%20WEBSHELL-2e3440?style=for-the-badge"/><br/>
Aizawa is a super simple command-line webshell that executes commands via the HTTP request in order to <b>avoid any WAF or IDS while bypassing disable_function</b>. The name Aizawa itself is taken from virtual youtuber <a href="https://www.youtube.com/channel/UCPkKpOHxEDcwmUAnRpIu-Ng">Aizawa Ema</a> from <a href="https://vspo.jp/">Virtual Esport Project</a>. Ema herself is a girl who likes bread and cats. She's always trying to improve her game skills. She wants to be a neat and tidy character, but is she really?<br/><br/><img src="https://img.shields.io/badge/PYTHON-3.10-bf616a?style=flat-square"/> <img src="https://img.shields.io/badge/LICENE-GPL2.0-ebcb8b?style=flat-square"/> <img src="https://img.shields.io/badge/VERSION-1.4.1-a3be8c?style=flat-square"/><br/><a href="https://www.paypal.com/paypalme/elliottophellia"><img src="https://img.shields.io/badge/BUY%20ME%20A%20COFFEE-79B8CA?style=for-the-badge&logo=paypal&logoColor=white"/></a> <a href="https://saweria.co/elliottophellia"><img src="https://img.shields.io/badge/TRAKTIR%20SAYA%20KOPI-FAC76C?style=for-the-badge&logo=BuyMeACoffee&logoColor=black"/></a>
</p>
<h1></h1>
<p align='center'>
<a href="#Changelogs"><img src="https://img.shields.io/badge/CHANGELOGS-2e3440?style=for-the-badge"/></a> <a href="#Prerequisites"><img src="https://img.shields.io/badge/PREREQUISITES-2e3440?style=for-the-badge"/></a> <a href="#Installing"><img src="https://img.shields.io/badge/INSTALLING-2e3440?style=for-the-badge"/></a> <a href="#Screenshot"><img src="https://img.shields.io/badge/SCREENSHOT-2e3440?style=for-the-badge"/></a> <a href="#References"><img src="https://img.shields.io/badge/REFERENCES-2e3440?style=for-the-badge"/></a> <a href="#Licence"><img src="https://img.shields.io/badge/LICENCE-2e3440?style=for-the-badge"/></a> <a href="#Disclaimer"><img src="https://img.shields.io/badge/DISCLAIMER-2e3440?style=for-the-badge"/></a>
</p>
<h1></h1>

# TODO - v2.0.0

# Minor
- [ ] Find a better code execution method with eval to replace the current one (aizawa_ninja_eval_.php) which not that effective in newer versions of PHP
- [ ] Find a PoC to bypass disable_function in PHP 8.2.X 

# Major
- [ ] Remove both HTTP_USER_AGENT and HTTP_ACCEPT_LANGUAGE methods entirely from the code base
- [ ] Replace httpx with HackRequests
- [ ] Replace Headers.create with random-header-generator
- [ ] Implement a http proxy rotator with support from [elliottophellia/yakumo](https://github.com/elliottophellia/yakumo) for each request to make it difficult to track
- [ ] Implement a replacement for HTTP_USER_AGENT and HTTP_ACCEPT_LANGUAGE which will be using AIZAWA_NINJA like the other NINJA Shell
- [ ] Moving the webshell itself into new repository to reduce confusion

# Misc
- [ ] Implement an Authentication for the webshells

# Prerequisites

- Python 3.10
- Pip 22.0.2 
- Httpx[http2] 0.25.0
- Validators 0.22.0

# Installing

### 1. Clone this repository
```
git clone http://github.com/elliottopellia/aizawa
```
### 2. Change directory to aizawa
```
cd aizawa
```
### 3. Install dependencies
```
Windows, Linux, Mac, Termux:
pip install -r requirements.txt

Arch Linux based:
pacman -S python-httpx python-validators python-h2
```
### 4. Run aizawa
```
python main.py / python main.py [webshell url]
```

# Screenshot

![1](./images/ss1.png)
![2](./images/ss2.png)

# References

- [s0md3v](https://github.com/s0md3v/nano)
- [Acunetix](https://bit.ly/AcunetiX)
- [mm0r1](https://github.com/mm0r1/exploits)

# Licence

This project is licensed under the GPL 2.0 License - see the [LICENCE](https://github.com/elliottophellia/aizawa/blob/main/LICENSE) file for details

# Disclaimer

This project is for educational purposes only. I will not be responsible for any misuse of this project by any party, or any damage caused by this project.

[<img src="https://api.gitsponsors.com/api/badge/img?id=574290720" height="20">](https://api.gitsponsors.com/api/badge/link?p=KFYbutSs0pvM3IDfCOxUy/k3GP0oy6rjbvn0jbTQXtJFoK301ViM2T8gDX7u8jufoUS2dProxfv9X49YMFEy1OlylREWQfiN5iRVgzC9t/EXFH2xObRnKkc15nef0PfCVZgaGNqlO9c4XS0z7kRUgj5JfTO5xlhj7JIpdcOWlDw=)
