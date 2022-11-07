from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path('project_projects/', views.project_projects, name="project_projects"),
    path('project_course/', views.project_course, name="project_course"),
    path('project_extra/', views.project_extra, name="project_extra"),
    path('project_research/', views.project_research , name='project_research'),
]
