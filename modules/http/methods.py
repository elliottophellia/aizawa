import base64
from .request import HttpRequest
from modules.utilities import Headers

class HttpMethods:
    @staticmethod
    async def http_accept_language_get(client, url, cmd):
        headers = Headers.create(None, cmd)
        return await HttpRequest.request(client, "get", url, headers)

    @staticmethod
    async def http_accept_language_post(client, url, data, cmd):
        headers = Headers.create(None, cmd)
        return await HttpRequest.request(client, "post", url, headers, data)

    @staticmethod
    async def http_aizawa_ninja(client, url, cmd):
        headers = Headers.create()
        headers["Aizawa-Ninja"] = base64.b64encode(cmd.encode("utf-8"))
        return await HttpRequest.request(client, "get", url, headers)

    @staticmethod
    async def http_user_agent_get(client, url, cmd):
        headers = Headers.create(cmd, None)
        return await HttpRequest.request(client, "get", url, headers)

    @staticmethod
    async def http_user_agent_post(client, url, data, cmd):
        headers = Headers.create(cmd, None)
        return await HttpRequest.request(client, "post", url, headers, data)