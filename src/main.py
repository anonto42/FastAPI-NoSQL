from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from src.utils.http_status_code import HTTP_STATUS
from src.error.exceptions_error import APIError
from src.templates.home_template import home_template
from src.error.global_error import global_error_handler
from src.error.json_error_hangler import api_json_error_handler

app = FastAPI(title="FastAPI")

# CORS 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Error exception middleware
app.add_exception_handler(APIError, api_json_error_handler)

# Global error handler middleware
@app.middleware("http")
async def global_error_handler_middleware(request, call_next):
    return await global_error_handler(request, call_next)

# Sample route
@app.get("/")
def read_root():
    return HTMLResponse(content=home_template(), status_code=HTTP_STATUS.OK)
