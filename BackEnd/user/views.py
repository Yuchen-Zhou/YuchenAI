from django.shortcuts import render
from django.http.request import HttpRequest
from django.http import JsonResponse


def register(request: HttpRequest):
    if request.method == 'POST':
        print(request.body)


def login(request: HttpRequest):
    if request.method == 'POST':
        print(request.body)
