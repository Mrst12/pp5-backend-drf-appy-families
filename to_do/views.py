'''views file for Todo page'''
from rest_framework import generics, permissions
from p5_drf_api.permissions import IsOwnerOrReadOnly
from .models import Todo
from .serializers import TodoSerializer


class TodoList(generics.ListCreateAPIView):
    '''list tasks or create tasks if logged in'''
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Todo.objects.all()

    def perform_create(self, serializer):
        '''make sure user associated with task'''
        serializer.save(owner=self.request.user)


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    '''retrieve, edit or delete a task if owned by user'''
    serializer_class = TodoSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Todo.objects.all()
