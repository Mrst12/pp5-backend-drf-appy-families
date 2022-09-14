'''database model for comments for memo posts'''
from django.db import models
from django.contrib.auth.models import User
from memo_posts.models import Memo


# class taken from the DRF_API walkthrough but modified
class MemoComment(models.Model):
    '''Comment model for memo_posts'''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    memo_post = models.ForeignKey(Memo, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        '''which order to place comments'''
        ordering = ['-created_on']

        def __str__(self):
            '''what to return'''
            return self.content
