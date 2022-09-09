''' profiles database '''
from django.db import models
from django.db.models.signals import post_save
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


# function taken from DRF-API walkthrough
def create_profile(sender, instance, created, **kwargs):
    ''' ensure a profile is created for each user created '''
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
