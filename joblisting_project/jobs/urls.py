from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_home, name='api_home'),                          # Default route for /api/
    path('jobs/', views.get_jobs, name='get_jobs'),                     # List all jobs
    path('jobs/create/', views.create_job, name='create_job'),          # Create a new job
    path('jobs/<int:pk>/', views.get_job_detail, name='get_job_detail'), # Retrieve, update, or delete a specific job
]
