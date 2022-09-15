'''models page for likes for the memo posts'''
from django.db import models
from django.contrib.auth.models import User
from memo_posts.models import Memo


# class taken from DRF_walkthrough challenge with modifications
class MemoLikes(models.Model):
    '''class to allow user to like memo posts'''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    memo_post = models.ForeignKey(
        Memo, related_name='like_memo', on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''how to order'''
        ordering = ['-created_on']
        unique_together = ['owner', 'memo_post']

    def __str__(self):
        '''what to return'''
        return f'{self.owner} {self.memo_post}'
