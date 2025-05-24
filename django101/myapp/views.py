from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import TodoItem


# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    """
    A simple view that returns a greeting message.
    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A simple HTTP response with a greeting message.
    """
    # return HttpResponse("Hello, world. You're at the myapp home page.")
    return render(request, "home.html")


def todos(request: HttpRequest) -> HttpResponse:
    """
    A simple view that returns a list of to-do items.
    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A simple HTTP response with a list of to-do items.
    """
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})
