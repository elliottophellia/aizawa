from .http_request import http_request
from modules.utils.headers import create_headers

async def http_user_agent_get(client, url, cmd):
    headers = create_headers(cmd, None)
    return await http_request(client, "get", url, headers)