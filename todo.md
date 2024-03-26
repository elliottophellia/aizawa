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