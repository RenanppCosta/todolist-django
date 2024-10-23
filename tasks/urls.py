from django.urls import path 
from tasks import views

urlpatterns = [
    path('', views.create_task, name='create_task'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('update', views.update_task, name='update_task')
]