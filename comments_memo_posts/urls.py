'''url file for memo posts comments'''
from django.urls import path
from comments_memo_posts import views

urlpatterns = [
    path('comments_memo_posts/', views.MemoCommentList.as_view()),
]
