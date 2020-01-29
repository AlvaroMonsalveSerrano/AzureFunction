import logging

import azure.functions as func
from datetime import datetime


def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    The FunctionBase is that function that is executed .

    Test Data Factory:
    + curl -v  -w '\n' -d '{"name":"pp"}' -H 'DateData: 2019/11/26' -H 'Content-Type: application/json' -X POST  http://localhost:7071/api/FunctionBase
    + curl -v  -w '\n' -d '{"name":"pp"}' -H 'DateData: 2019/11/26' -H 'Content-Type: application/json' -X POST  https://<URL-AZURE>.net/api/FunctionBase?code=<FUNCTION_KEY>

    """
    logging.info('Python HTTP trigger function processed a request.')
    datetime_object = datetime.strptime(req.headers.get('DateData'), '%Y/%m/%d')
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse('{ "test": "' + name + '", "date": "' + str(datetime_object) + '"}')
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )
