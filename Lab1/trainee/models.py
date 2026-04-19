from django.db import models


class Course(models.Model):
	name = models.CharField(max_length=100, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name


class Trainee(models.Model):
	name = models.CharField(max_length=150)
	age = models.IntegerField()
	email = models.EmailField(unique=True)
	course = models.ForeignKey(
		Course,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		related_name='trainees',
	)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return f'{self.name} ({self.email})'
