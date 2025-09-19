import azure.functions as func
import logging

app = func.FunctionApp()

# Standard function
@app.route(route="HelloFunction", auth_level=func.AuthLevel.ANONYMOUS)
def HelloFunction(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully!!!")
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200
        )

# Extra function for root URL (Browse button)
@app.route(route="", auth_level=func.AuthLevel.ANONYMOUS)
def RootFunction(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(
        "Welcome! This is the root of your Azure Function App. Try /api/HelloFunction?name=YourName",
        status_code=200
    )
