from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_trainees, name='trainee_list'),
    path('add/', views.add_trainee, name='add_trainee'),
    path('update/<int:id>/', views.update_trainee, name='update_trainee'),
    path('delete/<int:id>/', views.delete_trainee, name='delete_trainee'),
    path('detail/<int:id>/', views.trainee_detail, name='trainee_detail'),
]
