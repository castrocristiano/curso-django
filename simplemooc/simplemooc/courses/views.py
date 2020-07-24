from django.shortcuts import render, get_object_or_404
from .models import Course
from .forms import ContactCourse

POST = 'POST'
TEMPLATE_COURSES = 'courses/index.html'
TEMPLATE_DETAILS = 'courses/details.html'


def index(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, TEMPLATE_COURSES, context)

'''
    def details(request, pk):
        # course = Course.objects.get(pk=pk)
        course = get_object_or_404(Course, slug=pk)
        context = {
            'course': course
        }
        return render(request, TEMPLATE_DETAILS, context)
'''


def details(request, slug):
    # course = Course.objects.get(pk=pk)
    course = get_object_or_404(Course, slug=slug)
    context = {}
    if request.method == POST:
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            print(form.cleaned_data)
            form = ContactCourse()
    else:
        form = ContactCourse()
    context['course'] = course
    context['form'] = form
    return render(request, TEMPLATE_DETAILS, context)
