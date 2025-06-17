from server.error.exceptions_error import APIError
from server.constants.http_status_code import HTTP_STATUS

async def login(data):
    try:
        print(data)
        return 
        
    except Exception as err:
        print(err)
        raise APIError(HTTP_STATUS.Expectation_Failed)