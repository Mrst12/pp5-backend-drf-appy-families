'''database model for the likes for achievement page'''
from django.db import models
from django.contrib.auth.models import User
from achievements.models import Achievements


class AchievementLikes(models.Model):
    '''like model for the achievements page'''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    achievement_post = models.ForeignKey(
        Achievements, related_name='like_achievements',
        on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''how to order and user cant like same post twice'''
        ordering = ['-created_on']
        unique_together = ['owner', 'achievement_post']

    def __str__(self):
        '''what to display'''
        return f'{self.owner} {self.achievement_post}'
