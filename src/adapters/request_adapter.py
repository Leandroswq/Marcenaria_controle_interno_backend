from fastapi import Request
from src.models.http.request_model import HttpRequestModel
from pydantic import BaseModel
from typing import List


async def request_adapter(
    request: Request,
    body: BaseModel | dict = None,
    path_params: List[any] | None = None,
):
    header = request.headers
    query_params = request.query_params
    path_params = path_params
    url = str(request.url)
    ipv4 = request.client.host

    request_model = HttpRequestModel(
        header=header,
        body=body,
        query_params=query_params,
        path_params=path_params,
        url=url,
        ipv4=ipv4,
    )

    return request_model
