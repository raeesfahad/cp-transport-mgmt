from django.shortcuts import render,HttpResponse


def index(request):
    return HttpResponse("<h1>Test</h2>")


def login(login):
    return HttpResponse("<h1>Login</h2>")
