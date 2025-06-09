from fastapi import Request
from fastapi.responses import JSONResponse
from exceptions import APIError
import os, traceback, logging

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
                "message": ce.detail,
            }
        )
    except Exception as e:
        logging.error("Unhandled error: %s", str(e))
        tb = traceback.format_exc()
        traceback.print_exc()

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