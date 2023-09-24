from .http_request import http_request
from modules.utils.headers import create_headers

async def http_accept_language_get(client, url, cmd):
    headers = create_headers(None, cmd)
    return await http_request(client, "get", url, headers)