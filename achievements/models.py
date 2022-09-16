'''database models for achievements page'''
from django.db import models
from django.contrib.auth.models import User


class Achievements(models.Model):
    '''database model for achievements page'''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../achievement-image_e4ii4f',
        blank=True
    )

    class Meta:
        ''' how to order'''
        ordering = ['-date_created']

    def __str__(self):
        '''what to return'''
        return f'{self.id} {self.title}'
