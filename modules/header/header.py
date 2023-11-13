class Headers:
    """
        Create headers for an HTTP request.

        :param user_agent: (Optional) The User-Agent header value. Defaults to a standard Chrome user agent string.
        :type user_agent: str
        :param accept_language: (Optional) The Accept-Language header value. Defaults to "en-US,en;q=0.9".
        :type accept_language: str
        :return: The headers dictionary for the HTTP request.
        :rtype: dict
    """
    @staticmethod
    def create(user_agent=None, accept_language=None):
        headers = {
            "sec-ch-ua": 'Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": user_agent
            or "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": accept_language or "en-US,en;q=0.9",
        }
        return headers