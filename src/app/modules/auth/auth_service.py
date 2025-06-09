from src.error.exceptions_error import APIError
from src.constants.http_status_code import HTTP_STATUS

async def login():
    try:
        
        return "login successfully done!"\
        
    except Exception as err:
        print(err)
        raise APIError(HTTP_STATUS.Expectation_Failed)