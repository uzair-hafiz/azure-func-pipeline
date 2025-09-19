import azure.functions as func
import logging

app = func.FunctionApp()

# Root route
@app.route(route="", auth_level=func.AuthLevel.ANONYMOUS)
def HelloFunction(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            req_body = {}
        name = req_body.get('name')

    if name:
        return func.HttpResponse(
            f"Hello, {name}. This HTTP triggered function executed successfully!!!",
            status_code=200
        )
    else:
        return func.HttpResponse(
            "Hello there! This HTTP triggered function executed successfully. "
            "Pass a name in the query string (?name=YourName) or in the request body "
            "for a personalized response.",
            status_code=200
        )
