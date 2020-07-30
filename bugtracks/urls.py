"""Define URL patterns for bugtracks"""

from django.urls import path, include

from . import views

app_name = 'bugtracks'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Projects page
    path('projects/', views.projects, name='projects'),
    # Detail page for a project
    path('projects/<int:project_id>/', views.project, name='project'),
    # Page for adding a new project
    path('new_project/', views.new_project, name='new_project'),
]