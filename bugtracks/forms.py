from django import forms

from .models import Project, Ticket

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['text', 'in_progress']
        labels = {'text': '', 'in_progress': 'In progress:'}

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields =['priority', 'text', 'message']
        labesl = {'priority': 'Priority: ', 'text': '', 'message': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80}),
        'message': forms.Textarea(attrs={'cols': 80})}

class CompletedForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['text', 'message', 'ticket_progress']
        labesl = {'text': '', 'message': '', 'ticket_progress': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80}),
        'message': forms.Textarea(attrs={'cols': 80})}