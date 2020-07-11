from simplemooc.courses.models import Course


# https://docs.djangoproject.com/pt-br/3.0/ref/models/querysets/
django = Course(name='Python com Django', slug='django')
django.save()
django.pk

python_dev = Course(name='Python para Devs', slug='python-dev')
python_dev.save()
python_dev.pk

courses = Course.objects.all()
for course in courses:
    print(course.name)

courses = Course.objects.filter(slug='django')
for course in courses:
    print(course.name)

# https://docs.djangoproject.com/pt-br/3.0/ref/models/querysets/#icontains
courses = Course.objects.filter(name__icontains='WEB')
for course in courses:
    print(course.name)


for course in courses.all():
    print(course.name)

Course.objects.all()

courses.delete()
Course.objects.all()
