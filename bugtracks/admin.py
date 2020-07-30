from django.contrib import admin

from .models import Project, Ticket

admin.site.register(Project)
admin.site.register(Ticket)