'''url paths for likes for achievements page'''
from django.urls import path
from like_achievements import views


urlpatterns = [
    path('like_achievements/', views.AchievementLikesList.as_view()),
    path('like_achievements/<int:pk>/', views.AchievementLikesDetail.as_view()),
]
