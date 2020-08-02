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
    # Page for adding new tickets
    path('new_ticket/<int:project_id>/', views.new_ticket, name='new_ticket'),
    # Page for editing tickets
    path('edit_ticket/<int:ticket_id>/', views.edit_ticket, name='edit_ticket'),
    # Path for completing tickets
    path('completed_ticket/<int:ticket_id>/', views.completed_ticket, name='completed_ticket'),
    # Path for deleting tickets
]