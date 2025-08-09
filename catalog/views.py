import datetime

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Author, Book, LiteraryFormat


def hello_world(request: HttpRequest, unique_number: int) -> HttpResponse:
    now = datetime.datetime.now()
    query_params = request.GET
    print(f"Request method: {request.method}")
    print(f"Unique number: {unique_number}")
    print(f"Request params: {query_params}")
    return HttpResponse("<html>"
                        "<h1>Hello, world!</h1>"
                        f"<h4>Current moment: {now}</h4>"
                        f"<h4>Unique number: {unique_number}</h4>"
                        f"<h4>Request params: {query_params}</h4>"
                        "<html>")


def index(request: HttpRequest) -> HttpResponse:
    num_books = Book.objects.count()
    num_authors = Author.objects.count()
    num_literary_formats = LiteraryFormat.objects.count()
    context = {
        "num_books": num_books,
        "num_authors": num_authors,
        "num_literary_formats": num_literary_formats,
    }
    return render(request, "catalog/index.html", context=context)
