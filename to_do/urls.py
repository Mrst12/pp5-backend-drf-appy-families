'''url paths for the Todo app'''
from django.urls import path
from to_do import views

urlpatterns = [
    path('to_do/', views.TodoList.as_view()),
]