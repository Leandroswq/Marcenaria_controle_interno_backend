from pydantic import BaseModel
from typing import Optional


def no_body_response_model_factory(response_message: str):
    class NoBodyResponseModel(BaseModel):
        detail: str = response_message

    return NoBodyResponseModel


def response_model_factory(
    response_data: object,
    response_message: str = "Operação efetuada com sucesso",
) -> object:
    class NoBodyResponseModel(BaseModel):
        detail: Optional[str] = response_message
        data: response_data

    return NoBodyResponseModel


Delete_response_model = no_body_response_model_factory("Excluido com sucesso")
Insert_response_model = no_body_response_model_factory("Inserido com sucesso")
Update_response_model = no_body_response_model_factory("Atualizado com sucesso")
