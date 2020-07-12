from django.shortcuts import render, get_object_or_404
from simplemooc.courses.models import Course

TEMPLATE_COURSES = 'courses/index.html'
TEMPLATE_DETAILS = 'courses/details.html'


def index(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, TEMPLATE_COURSES, context)


def details(request, pk):
    # course = Course.objects.get(pk=pk)
    course = get_object_or_404(Course, pk=pk)
    context = {
        'course': course
    }
    return render(request, TEMPLATE_DETAILS, context)
