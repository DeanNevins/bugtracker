from django.db import models
from django.db.models.deletion import SET_NULL
from django.utils import timezone

from users.models import Employee

# Create your models here.

class Ticket(models.Model):
    NEW = 'New'
    IN_PROGRESS = 'In Progress'
    DONE = 'Done'
    INVALID = 'Invalid'
    STATUS_CHOICES = [
        (NEW, 'New'),
        (IN_PROGRESS, 'In Progress'),
        (DONE, 'Done'),
        (INVALID, 'Invalid')
    ]
    title = models.CharField(max_length=150)
    date_filed = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    creator = models.ForeignKey(Employee, related_name="related_creator_ticket", on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=NEW)
    assigned_to = models.ForeignKey(Employee, related_name="related_assigned_to", null=True, blank=True, on_delete=models.SET_NULL)
    completed_by = models.ForeignKey(Employee, related_name="related_completed_by", null=True, blank=True, on_delete=models.SET_NULL)
    completed_before = models.BooleanField(default=False)

    def __str__(self):
        return self.title
