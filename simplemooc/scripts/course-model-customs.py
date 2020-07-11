from simplemooc.courses.models import Course

''' https://docs.djangoproject.com/pt-br/3.0/ref/models '''
Course.objects.all()

Course.objects.create(name='Python com Django', slug='django')
Course.objects.create(name='Python para devs', slug='python')
Course.objects.create(name='Lógica de programação', slug='logica')

Course.objects.search('python')

courses = Course.objects.search('python')
for c in courses:
    print(c.name)
