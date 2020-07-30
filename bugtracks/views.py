from django.shortcuts import render, redirect

from .models import Project, Ticket
from .forms import ProjectForm

def index(request):
    """The home page for bugtracks"""
    return render(request, 'bugtracks/index.html')

def projects(request):
    """Show all projects"""
    projects = Project.objects.order_by('date_added')
    context = {'projects': projects}
    return render(request, 'bugtracks/projects.html', context)

def project(request, project_id):
    """Show a project and all it's tickets"""
    project = Project.objects.get(id=project_id)
    tickets = project.ticket_set.order_by('-date_added')
    context = {'project': project, 'tickets': tickets}
    return render(request, 'bugtracks/project.html', context)

def new_project(request):
    """Add a new project"""
    if request.method != 'POST':
        # No data submitted; create blank form
        form = ProjectForm()
    else:
        # POST data submitted; process data
        form = ProjectForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('bugtracks:projects')
    
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'bugtracks/new_project.html', context)