import base64
from .http_request import http_request
from modules.utils.headers import create_headers

async def http_aizawa_ninja(client, url, cmd):
    headers = create_headers()
    headers["Aizawa-Ninja"] = base64.b64encode(cmd.encode("utf-8"))
    return await http_request(client, "get", url, headers)