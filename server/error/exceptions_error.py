import traceback
from fastapi import HTTPException

class APIError(HTTPException):
    def __init__(self, status_code: int, message: str, path: str = None):
        
        stack_trace = traceback.format_exc() 

        if path is None:
            path = "Unknown Path"

        self.detail = {
            "message": message,
            "stack_trace": stack_trace,
            "path": path
        }

        super().__init__(status_code=status_code, detail=self.detail)
