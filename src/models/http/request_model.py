class HttpRequestModel:
    def __init__(
        self,
        header=None,
        body=None,
        query_params=None,
        path_params=None,
        url=None,
        ipv4=None,
    ) -> None:
        self.header = header
        self.body = body
        self.query_params = query_params
        self.path_params = path_params
        self.url = url
        self.ipv4 = ipv4
        self.path_params = path_params
