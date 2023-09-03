<p align='center'>
<img src='./images/aizawa.png' width='300'/><br/><img src="https://img.shields.io/badge/AIZAWA%20BYPASS%20WEBSHELL-2e3440?style=for-the-badge"/><br/>
Aizawa is a super simple command-line webshell that executes commands via the HTTP request in order to <b>avoid any WAF or IDS while bypassing disable_function</b>. The name Aizawa itself is taken from virtual youtuber <a href="https://www.youtube.com/channel/UCPkKpOHxEDcwmUAnRpIu-Ng">Aizawa Ema</a> from <a href="https://vspo.jp/">Virtual Esport Project</a>. Ema itself is a girl who likes bread and cats. She's always trying to improve her game skills. She wants to be a neat and tidy character, but is she really?<br/><br/><img src="https://img.shields.io/badge/PHP-7.4-bf616a?style=flat-square"/> <img src="https://img.shields.io/badge/LICENE-GPL2.0-ebcb8b?style=flat-square"/> <img src="https://img.shields.io/badge/VERSION-1.2.0-a3be8c?style=flat-square"/><br/><a href="https://www.paypal.com/paypalme/elliottophellia"><img src="https://img.shields.io/badge/BUY%20ME%20A%20COFFEE-79B8CA?style=for-the-badge&logo=paypal&logoColor=white"/></a> <a href="https://saweria.co/elliottophellia"><img src="https://img.shields.io/badge/TRAKTIR%20SAYA%20KOPI-FAC76C?style=for-the-badge&logo=BuyMeACoffee&logoColor=black"/></a>
</p>
<h1></h1>
<p align='center'>
<a href="#Changelogs"><img src="https://img.shields.io/badge/CHANGELOGS-2e3440?style=for-the-badge"/></a> <a href="#Prerequisites"><img src="https://img.shields.io/badge/PREREQUISITES-2e3440?style=for-the-badge"/></a> <a href="#Installing"><img src="https://img.shields.io/badge/INSTALLING-2e3440?style=for-the-badge"/></a> <a href="#Screenshot"><img src="https://img.shields.io/badge/SCREENSHOT-2e3440?style=for-the-badge"/></a> <a href="#References"><img src="https://img.shields.io/badge/REFERENCES-2e3440?style=for-the-badge"/></a> <a href="#Licence"><img src="https://img.shields.io/badge/LICENCE-2e3440?style=for-the-badge"/></a> <a href="#Disclaimer"><img src="https://img.shields.io/badge/DISCLAIMER-2e3440?style=for-the-badge"/></a>
</p>
<h1></h1>

# Changelogs - v1.2.0

- Added NINJA CONCAT edition
- Added NINJA USER_FILTER edition
- Added NINJA GARBAGE_COLLECTOR edition
- Added NINJA JSON_SERIALIZER edition
- Added NINJA DEBUG_BACKTRACE edition
- Fix bug in interactive shell that causes entire line to be deleted when pressing backspace
- Fix bug in interactive shell that causes hostname displayed as $user when server response with null instead of $hostname


## What are those editions?

### NINJA CONCAT
This exploit uses a [bug](https://bugs.php.net/bug.php?id=81705) in a function that handles string concatenation. A statement such as `$a.$b` might result in memory corruption if certain conditions are met. The bugreport provides a very thorough analysis of the vulnerability. 

The PoC was tested on various php builds for Debian/Ubuntu/CentOS/FreeBSD with cli/fpm/apache2 server APIs and found to work reliably.

#### Targets
  - 7.3 - all versions to date
  - 7.4 - all versions to date
  - 8.0 - all versions to date
  - 8.1 - all versions to date

Credits to [@mm0r1](https://github.com/mm0r1) for the PoC

### NINJA USER_FILTER
This exploit uses a [bug](https://bugs.php.net/bug.php?id=54350) **reported over 10 years ago**. As usual, the PoC was tested on various php builds for Debian/Ubuntu/CentOS/FreeBSD with cli/fpm/apache2 server APIs and found to work reliably.

#### Targets
  - 5.* - exploitable with minor changes to the PoC
  - 7.0 - all versions to date
  - 7.1 - all versions to date
  - 7.2 - all versions to date
  - 7.3 - all versions to date
  - 7.4 < 7.4.26
  - 8.0 < 8.0.13

Credits to [@mm0r1](https://github.com/mm0r1) for the PoC

### NINJA GARBAGE_COLLECTOR
This exploit uses a three year old [bug](https://bugs.php.net/bug.php?id=72530) in PHP garbage collector to bypass `disable_functions` and execute a system command. It was tested on various php7.0-7.3 builds for Ubuntu/CentOS/FreeBSD with cli/fpm/apache2 server APIs and found to work reliably. Feel free to submit an issue if you experience any problems.

#### Targets
  - 7.0 - all versions to date
  - 7.1 - all versions to date
  - 7.2 - all versions to date
  - 7.3 - all versions to date

Credits to [@mm0r1](https://github.com/mm0r1) for the PoC

### NINJA JSON_SERIALIZER
This exploit utilises a use after free [vulnerability](https://bugs.php.net/bug.php?id=77843) in json serializer in order to bypass `disable_functions` and execute a system command. It should be fairly reliable and work on all server apis, although that is not guaranteed.

#### Targets
  - 7.1 - all versions to date
  - 7.2 < 7.2.19 (released: 30 May 2019)
  - 7.3 < 7.3.6 (released: 30 May 2019)

Credits to [@mm0r1](https://github.com/mm0r1) for the PoC and [@cfreal](https://github.com/cfreal) for the original bug discovery.

### NINJA DEBUG_BACKTRACE
This exploit uses a two year old [bug](https://bugs.php.net/bug.php?id=76047) in debug_backtrace() function. We can trick it into returning a reference to a variable that has been destroyed, causing a use-after-free vulnerability. The PoC was tested on various php builds for Debian/Ubuntu/CentOS/FreeBSD with cli/fpm/apache2 server APIs and found to work reliably.

#### Targets
  - 7.0 - all versions to date
  - 7.1 - all versions to date
  - 7.2 - all versions to date
  - 7.3 < 7.3.15 (released 20 Feb 2020)
  - 7.4 < 7.4.3 (released 20 Feb 2020)

Credits to [@mm0r1](https://github.com/mm0r1) for the PoC

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

# References

- [s0md3v](https://github.com/s0md3v/nano)
- [Acunetix](https://bit.ly/AcunetiX)
- [Peter Krauss](https://stackoverflow.com/posts/2929951/revisions)
- [Tim Post](https://stackoverflow.com/posts/2929951/revisions)
- [mm0r1](https://github.com/mm0r1)

# Licence

This project is licensed under the GPL 2.0 License - see the [LICENCE](https://github.com/elliottophellia/aizawa/blob/main/LICENSE) file for details

# Disclaimer

This project is for educational purposes only. I will not be responsible for any misuse of this project by any party, or any damage caused by this project.

