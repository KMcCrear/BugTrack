from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Project, Ticket
from .forms import ProjectForm, TicketForm, CompletedForm

def index(request):
    """The home page for bugtracks"""
    return render(request, 'bugtracks/index.html')

@login_required
def projects(request):
    """Show all projects"""
    projects = Project.objects.order_by('date_added')
    context = {'projects': projects}
    return render(request, 'bugtracks/projects.html', context)

@login_required
def project(request, project_id):
    """Show a project and all it's tickets"""
    project = Project.objects.get(id=project_id)
    tickets = project.ticket_set.order_by('-date_added')
    no_tickets = Ticket.objects.filter(project_id=project_id).count()
    context = {'project': project, 'tickets': tickets, 'no_tickets': no_tickets}
    return render(request, 'bugtracks/project.html', context)

@login_required
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

@login_required
def new_ticket(request, project_id):
    """Submitting a new ticket to a particular project"""
    project = Project.objects.get(id=project_id)

    if request.method != 'POST':
        # No data submitted; create blank form
        form = TicketForm()
    else:
        #POST data submitted; process data
        form = TicketForm(data=request.POST)
        if form.is_valid():
            new_ticket = form.save(commit=False)
            new_ticket.project = project
            new_ticket.save()
            return redirect('bugtracks:project', project_id=project_id)
    
    #Display a blank or invalid form
    context = {'project': project, 'form': form}
    return render(request, 'bugtracks/new_ticket.html', context)

@login_required
def edit_ticket(request, ticket_id):
    """Edit an exisitng ticket"""
    ticket = Ticket.objects.get(id=ticket_id)
    project = ticket.project

    if request.method != 'POST':
        # Inital request; pre-fill form with current ticket
        form = TicketForm(instance=ticket)
    else:
        # POST data submitted; process data
        if request.method == 'POST' and 'save' in request.POST:
            form = TicketForm(instance=ticket, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('bugtracks:project', project_id=project.id)
        if request.method == 'POST' and 'delete' in request.POST:
            form = TicketForm(instance=ticket, data=request.POST)
            if form.is_valid():
                tk_delete = Ticket.objects.filter(id=ticket_id).delete()
                return redirect('bugtracks:project', project_id=project.id)
            
    
    context = {'ticket': ticket, 'project': project, 'form': form}
    return render(request, 'bugtracks/edit_ticket.html', context)
    
@login_required
def completed_ticket(request, ticket_id):
    """Mark a ticket as complete"""
    ticket = Ticket.objects.get(id=ticket_id)
    project = ticket.project

    if request.method != 'POST':
        # Inital request; pre-fill form with current data
        form = CompletedForm(instance=ticket)
    else:
        form = CompletedForm(instance=ticket, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('bugtracks:project', project_id=project.id)

    context = {'ticket': ticket, 'project': project, 'form': form}
    return render(request, 'bugtracks/completed_ticket.html', context)
