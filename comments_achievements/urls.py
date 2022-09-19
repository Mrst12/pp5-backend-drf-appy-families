'''url paths for comments for achievements'''
from django.urls import path
from comments_achievements import views


urlpatterns = [
    path('comments_achievements/', views.AchievementsCommentList.as_view()),
    path('comments_achievements/<int:pk>/', views.AchievementsCommentDetail.as_view()),
]
