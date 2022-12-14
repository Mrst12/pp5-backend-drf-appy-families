'''database models file for the to_do page'''
from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    '''Todo model for the Todo page'''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    task_title = models.CharField(max_length=250)
    content = models.TextField()
    due_date = models.DateField(null=True)

    class Meta:
        '''how to order'''
        ordering = ['-created_on']

    def __str__(self):
        '''what to display'''
        return f'{self.task_title}'
