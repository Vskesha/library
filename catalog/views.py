import datetime

from django.http import HttpRequest, HttpResponse


def hello_world(request: HttpRequest, unique_number: int) -> HttpResponse:
    now = datetime.datetime.now()
    print(f"Request method: {request.method}")
    print(f"Unique number: {unique_number}")
    query_params = request.GET
    return HttpResponse("<html>"
                        "<h1>Hello, world!</h1>"
                        f"<h4>Current moment: {now}</h4>"
                        f"<h4>Request params: {query_params}</h4>"
                        "<html>")
