'''url paths for achievements app'''
from django.urls import path
from achievements import views


urlpatterns = [
    path('achievements/', views.AchievementList.as_view()),
]