from django.http import HttpResponse


def foo(r) -> HttpResponse:
    return HttpResponse("Hello")
    