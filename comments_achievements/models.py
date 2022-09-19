'''database model for comments for the achievements page'''
from django.db import models
from django.contrib.auth.models import User
from achievements.models import Achievements


class AchievementsComment(models.Model):
    '''model for comments for achievements page'''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    achievement_post = models.ForeignKey(
        Achievements, on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        '''how to order content'''
        ordering = ['-created_on']

    def __str__(self):
        '''what to display'''
        return self.content
