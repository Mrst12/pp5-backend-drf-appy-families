''' profiles database '''
from django.db import models
from django.contrib.auth.models import User

# some code provided by DRF-API walkthrough
# modifications made for this project


class Profile(models.Model):
    '''Profile model for database'''
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        upload_to='images/',
        default='../default_profile_x5mrcs',
    )
    bio = models.TextField(blank=True)

    class Meta:
        ''' displaying newest first profile '''
        ordering = ['-created_on']

    def __str__(self):
        ''' shows what to display '''
        return f"{self.owner}'s profile."
