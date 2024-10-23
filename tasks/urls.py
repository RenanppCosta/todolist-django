from django.urls import path 
from tasks import views

urlpatterns = [
    path('', views.create_task, name='create_task'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('update', views.update_task, name='update_task'),
    path('check_task', views.check_task_is_completed, name='check_task_is_completed')
]