from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from server.constants.http_status_code import HTTP_STATUS
from server.error.exceptions_error import APIError
from server.templates.home_template import home_template
from server.error.global_error import global_error_handler
from server.error.json_error_handler import api_json_error_handler
from server.routes.api_router_v1 import router_v1
from server.db.db_connection import init_db

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

# Global error handler middleware
@app.middleware("http")
async def global_error_handler_middleware(request, call_next):
    return await global_error_handler(request, call_next)

# Initialize the database connection
@app.on_event("startup")
async def startup_db():
    db_info = init_db()
    app.mongo = db_info

# Sample route
@app.get("/")
def read_root():
    return HTMLResponse(content=home_template(), status_code=HTTP_STATUS.OK)

# Route intery poient
app.include_router(router_v1, prefix="/api/v1")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()
