# Minor
- [ ] Find a better code execution method with eval to replace the current one which not that effective in newer versions of PHP

# Major
- [ ] Remove both HTTP_USER_AGENT and HTTP_ACCEPT_LANGUAGE methods entirely from the code base, as they are not needed and not that efficient, prefer to make simple GET/POST one with custom http headers which also more secure
- [ ] Replace httpx with other libraries that have javascript support in case there is waf that checks javascript