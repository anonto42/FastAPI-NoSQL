from fastapi import Request
from fastapi.responses import JSONResponse
from server.error.exceptions_error import APIError

async def api_json_error_handler(request: Request, exc: APIError):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.detail["message"],
            "path": str(request.url.path),
            "stack_trace": exc.detail["stack_trace"],
        }
    )