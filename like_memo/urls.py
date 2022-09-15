'''url paths for memo post likes'''
from django.urls import path
from like_memo import views


urlpatterns = [
    path('like_memo/', views.MemoLikesList.as_view()),
]
