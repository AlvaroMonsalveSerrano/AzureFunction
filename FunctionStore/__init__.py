import logging

import azure.functions as func
from datetime import datetime


def main(request: func.HttpRequest, inputblob: func.InputStream, blobout: func.Out[func.InputStream], context: func.Context) -> func.HttpResponse:
    """
    The FunctionStore function performs the copying of an existing file in a Store to the same Store whose name is passed in the HTTP request.

    This function is a descriptive example of Azure App.

    curl -v -w '\n' -H 'DateData: 2019/11/26' -d '{ "param1": "value1", "param2": "value2" }'   -X GET http://localhost:7071/api/FunctionStore/watermark?name=11

    """
    logging.info('Python HTTP trigger function processed a request.')

    logging.info(f'[-->>]context.function_directory={context.function_directory}.')
    logging.info(f'[-->>]context.function_name={context.function_name}.')
    logging.info(f'[-->>]context.invocation_id={context.invocation_id}.')

    logging.info(f"Params: {request.params}")
    logging.info(f"Route Params: {request.route_params}")
    logging.info(f"Body: {request.get_body()}")

    logging.info(f"Headers: {request.headers}")
    logging.info(f"Headers: {request.headers.get('DateData')}")
    datetime_object = datetime.strptime(request.headers.get('DateData'), '%Y/%m/%d')
    logging.info(f"Fecha: {datetime_object}")

    name = datetime_object
    if not name:
        try:
            req_body = request.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    blobout.set(inputblob)

    if name:
        return func.HttpResponse(f"Hello {name}!")
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )
