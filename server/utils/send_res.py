from fastapi.responses import JSONResponse
from typing import Any, Optional

def send_response(
    success: bool = True,
    message: str = "",
    data: Optional[Any] = None,
    status_code: int = 200
) -> JSONResponse:
    """
    Returns a formatted JSON response.
    
    Args:
        success (bool): Indicates if the request was successful.
        message (str): Message for the client.
        data (Any): Any data to return.
        status_code (int): HTTP status code.

    Returns:
        JSONResponse: FastAPI JSON response.
    """
    return JSONResponse(
        status_code=status_code,
        content={
            "success": success,
            "message": message,
            "data": data,
        }
    )