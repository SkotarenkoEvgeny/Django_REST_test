from django.contrib import admin

from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')
    list_filter = ('name', 'start_date', 'end_date')
    search_fields = ('name', 'start_date', 'end_date')
