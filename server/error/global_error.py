import traceback
from fastapi import Request
from fastapi.responses import JSONResponse
from server.error.exceptions_error import APIError
import logging
import os

ENV = os.getenv("ENV", "development")

async def global_error_handler(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except APIError as ce:
        
        return JSONResponse(
            status_code=ce.status_code,
            content={
                "success": False,
                "message": ce.detail["message"],
                "stack_trace": ce.detail["stack_trace"], 
                "path": ce.detail["path"], 
            }
        )
    except Exception as e:
        
        logging.error("Unhandled error: %s", str(e))
        tb = traceback.format_exc()

        error_response = {
            "success": False,
            "message": "Internal Server Error",
        }

        if ENV == "development":
            error_response["detail"] = str(e)
            error_response["traceback"] = tb

        return JSONResponse(
            status_code=500,
            content=error_response
        )
