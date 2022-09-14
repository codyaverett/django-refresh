from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# request handler
# action


def say_hello(request) -> HttpResponse:
    # Pull data from db
    # Transform
    # Send email
    # ...
    return HttpResponse('Hello World')


def say_hello_to(request, name) -> HttpResponse:
    return render(request, 'hello.html', {'name': name})
