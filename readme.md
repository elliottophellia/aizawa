<p align='center'>
<img src='./images/aizawa.png' width='300'/><br/><img src="https://img.shields.io/badge/AIZAWA%20BYPASS%20WEBSHELL-2e3440?style=for-the-badge"/><br/><img src="https://img.shields.io/badge/PHP-8.2-bf616a?style=flat-square"/> <img src="https://img.shields.io/badge/LICENE-GPL2.0-ebcb8b?style=flat-square"/> <img src="https://img.shields.io/badge/VERSION-1.1.0-a3be8c?style=flat-square"/><br/><img src="https://img.shields.io/badge/BY%20ELLIOTTOPHELLIA-2e3440?style=flat-square"/>
</p>
<h1></h1>
<p align='center'>
<a href="#About"><img src="https://img.shields.io/badge/ABOUT-2e3440?style=for-the-badge"/></a> <a href="#Prerequisites"><img src="https://img.shields.io/badge/PREREQUISITES-2e3440?style=for-the-badge"/></a> <a href="#Installing"><img src="https://img.shields.io/badge/INSTALLING-2e3440?style=for-the-badge"/></a> <a href="#Screenshot"><img src="https://img.shields.io/badge/SCREENSHOT-2e3440?style=for-the-badge"/></a> <a href="#References"><img src="https://img.shields.io/badge/REFERENCES-2e3440?style=for-the-badge"/></a> <a href="#Licence"><img src="https://img.shields.io/badge/LICENCE-2e3440?style=for-the-badge"/></a> <a href="#Disclaimer"><img src="https://img.shields.io/badge/DISCLAIMER-2e3440?style=for-the-badge"/></a>
</p>
<h1></h1>

```
Note:
- NINJA edition as far as I know is not gonna work on PHP 7+
- GET/POST edition is working just fine on PHP 7+

Changelogs - v1.1.0

- Removed HEX encoding webshell
- Removed function.php and just put it in aizawa.php
- Refactored the function to be more efficient and simple
- Changed the way to recognize other webshell extention not just .php
- Added new way to execute commands in webshell with proc_open and popen
- Added an actually useful error message not like before
- Added an actually useful readme.md not like before
```

# About

Aizawa is a super simple command-line webshell that executes commands via the HTTP request in order to avoid any WAF or IDS. The name Aizawa itself is taken from virtual youtuber [Aizawa Ema](https://www.youtube.com/channel/UCPkKpOHxEDcwmUAnRpIu-Ng) from [Virtual Esport Project](https://vspo.jp/). Ema itself is a girl who likes bread and cats. She's always trying to improve her game skills. She wants to be a neat and tidy character, but is she really?

# Prerequisites

- PHP 7.4 or higher
- PHP cURL

# Installing

## 1. Clone this repository
```
git clone http://github.com/elliottopellia/aizawa
```
## 2. Change directory to aizawa
```
cd aizawa
```
## 3. Run aizawa
```
php aizawa.php / php aizawa.php [webshell url]
```
```
NOTE: The one who will be uploaded is the webshell that is in the webshell folder NOT THE AIZAWA.PHP ITSELF
```

# Screenshot

![1](./images/1.png)
![2](./images/2.png)
![3](./images/3.png)
![4](./images/4.png)

# References

- [s0md3v](https://github.com/s0md3v/nano)
- [Acunetix](https://bit.ly/AcunetiX)
- [Peter Krauss](https://stackoverflow.com/posts/2929951/revisions)
- [Tim Post](https://stackoverflow.com/posts/2929951/revisions)

# Licence

This project is licensed under the GPL 2.0 License - see the [LICENCE](https://github.com/elliottophellia/aizawa/blob/main/LICENSE) file for details

# Disclaimer

This project is for educational purposes only. I will not be responsible for any misuse of this project by any party, or any damage caused by this project.

