from django.conf.urls import url
from simplemooc.courses.views import index, details

urlpatterns = [
    # url(r'^$', views.home, name='home'),
    url(r'^$', index, name='index'),
    url(r'^(?P<pk>\d+)/$', details, name='details'),
]
