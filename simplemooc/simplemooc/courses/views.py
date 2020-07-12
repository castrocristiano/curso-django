from django.shortcuts import render
from simplemooc.courses.models import Course

TEMPLATE_NAME = 'courses/index.html'


def index(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, TEMPLATE_NAME, context)
