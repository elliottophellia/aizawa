from .http_request import http_request
from modules.utils.headers import create_headers

async def http_accept_language_post(client, url, data, cmd):
    headers = create_headers(None, cmd)
    return await http_request(client, "post", url, headers, data)