from fastapi import HTTPException


class ValidationException(HTTPException):
    def __init__(self):
        super().__init__(status_code=422, detail="Validation Error")


class NotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="Not Found Error")


class ConflictError(HTTPException):
    def __init__(self, detail):
        super().__init__(
            status_code=409,
            detail=detail,
        )
