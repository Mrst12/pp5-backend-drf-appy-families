''' database model for memo posts '''
from django.db import models
from django.contrib.auth.models import User


# class taken from DRF_API walkthrough modifications made
class Memo(models.Model):
    ''' memo posts model '''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    For = models.CharField(max_length=100)
    content = models.TextField(blank=True)

    class Meta:
        '''order by created on field'''
        ordering = ['created_on']

        def __str__(self):
            ''' shows what to display '''
            return f'{self.id} {self.For}'
