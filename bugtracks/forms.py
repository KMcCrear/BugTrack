from django import forms

from .models import Project, Ticket

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['text', 'in_progress']
        labels = {'text': '', 'in_progress': 'In progress:'}