from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TraineeForm
from .models import Trainee


def list_trainees(request):
	trainees = Trainee.objects.select_related('course').all()
	return render(request, 'trainee/list.html', {'trainees': trainees})


def add_trainee(request):
	if request.method == 'POST':
		form = TraineeForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Trainee added successfully.')
			return redirect('trainee_list')
	else:
		form = TraineeForm()

	return render(request, 'trainee/add.html', {'form': form})


def update_trainee(request, id):
	trainee = get_object_or_404(Trainee, pk=id)

	if request.method == 'POST':
		form = TraineeForm(request.POST, instance=trainee)
		if form.is_valid():
			form.save()
			messages.success(request, 'Trainee updated successfully.')
			return redirect('trainee_list')
	else:
		form = TraineeForm(instance=trainee)

	return render(request, 'trainee/update.html', {'form': form, 'trainee': trainee})


def delete_trainee(request, id):
	trainee = get_object_or_404(Trainee, pk=id)

	if request.method == 'POST':
		trainee.delete()
		messages.success(request, 'Trainee deleted successfully.')
		return redirect('trainee_list')

	return render(request, 'trainee/delete.html', {'trainee': trainee})


def trainee_detail(request, id):
	trainee = get_object_or_404(Trainee.objects.select_related('course'), pk=id)
	return render(request, 'trainee/detail.html', {'trainee': trainee})
