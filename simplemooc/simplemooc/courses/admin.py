from django.contrib import admin
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date', 'created_at', 'id']
    search_fields = ['id', 'name', 'slug']
    prepopulated_fields = {'slug': ['name']}


admin.site.register(Course, CourseAdmin)

