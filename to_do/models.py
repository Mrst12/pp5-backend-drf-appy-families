'''database models file for the to_do page'''
from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    '''Todo model for the Todo page'''
    status_choices = [
        ('pending', 'Pending'),
        ('started', 'Started'),
        ('done', 'Done')
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    task_title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    due_date = models.DateField(null=True)
    status = models.CharField(
        max_length=20, choices=status_choices, default='pending'
    )
    urgent = models.BooleanField(null=True)

    class Meta:
        '''how to order'''
        ordering = ['-created_on']

    def __str__(self):
        '''what to display'''
        return f'{self.task_title}'
