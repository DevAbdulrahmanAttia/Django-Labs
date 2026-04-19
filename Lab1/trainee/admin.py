from django.contrib import admin

from .models import Course, Trainee


@admin.register(Trainee)
class TraineeAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'age', 'email', 'course', 'created_at')
	search_fields = ('name', 'email')
	list_filter = ('course', 'created_at')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'created_at')
	search_fields = ('name',)
