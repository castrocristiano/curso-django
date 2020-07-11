from django.shortcuts import render

TEMPLATE_NAME = 'courses/index.html'


def index(request):
    return render(request, TEMPLATE_NAME)
