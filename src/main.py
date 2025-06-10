from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from src.constants.http_status_code import HTTP_STATUS
from src.error.exceptions_error import APIError
from src.templates.home_template import home_template
from src.error.global_error import global_error_handler
from src.error.json_error_hangler import api_json_error_handler
from src.routes.api_router_v1 import router_v1
from src.db import db_connection

app = FastAPI(title="FastAPI")

# CORS configarations
origins = [
    "*"
]

methods = [
    # "GET",
    # "POST"
    "*"
]

headers = [
    "*"
]

# CORS 
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=methods,
    allow_headers=headers,
)

# Error exception middleware
app.add_exception_handler(APIError, api_json_error_handler)

# Setup on DB on startup
@app.on_event("startup")
def on_startup():
    db_connection.on_startup()

# Global error handler middleware
@app.middleware("http")
async def global_error_handler_middleware(request, call_next):
    return await global_error_handler(request, call_next)

# Sample route
@app.get("/")
def read_root():
    return HTMLResponse(content=home_template(), status_code=HTTP_STATUS.OK)

# Route intery poient
app.include_router(router_v1, prefix="/api/v1")