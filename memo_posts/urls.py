'''urls for the memo posts'''
from django.urls import path
from memo_posts import views


urlpatterns = [
    path('memo_posts/', views.MemoList.as_view()),
    path('memo_posts/<int:pk>/', views.MemoDetail.as_view()),
]
