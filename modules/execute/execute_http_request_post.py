async def execute_http_request_post(client, url, cmd, method, request_func):
    result = await request_func(client, url, method, cmd)
    if result:
        return result
    return None