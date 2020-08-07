from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    """A project a user is working on"""
    YES = 'YES'
    NO = 'NO'
    PROGRESS_CHOICES = [
        (YES, 'Yes'),
        (NO, 'No')
    ]
    text = models.CharField(max_length=200)
    in_progress = models.CharField(max_length=3,
    choices=PROGRESS_CHOICES, default=YES)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model"""
        return self.text
    
    def check_progress(self):
        return self.in_progress

class Ticket(models.Model):
    """Tickets reporting bugs"""
    # Priortiry levels
    HIGH = 'HIGH'
    MEDIUM = 'MEDIUM'
    LOW = 'LOW'
    SUBMITTED = 'submitted'
    IN_DEV = 'In progress'
    COMPLETED = 'Completed'
    PRIORITY_CHOICES = [
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low')
    ]
    TICKET_PROGRESS = [
        (SUBMITTED, 'Submitted'),
        (IN_DEV, 'In progress'),
        (COMPLETED, 'Completed')
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    bug = models.CharField(max_length=300)
    text = models.TextField()
    message = models.TextField()
    priority = models.CharField(max_length=6,
    choices=PRIORITY_CHOICES,
    default=MEDIUM)
    ticket_progress = models.CharField(max_length=20,
    choices=TICKET_PROGRESS, default=SUBMITTED)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural ='tickets'
    

    def __str__(self):
        return f"{self.text[:50]}..."
    
    def check_priority(self):
        return self.priority
    
    def bug_return(self):
        return self.bug
