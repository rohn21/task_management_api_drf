from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from manage_task.serializers import TaskSerializer
from manage_task.models import Task

class TaskListCreateView(ListCreateAPIView):
    queryset = Task.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    pagination_class = PageNumberPagination
    
    # specific permission that only AdminUser can create task
    '''def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]
        return [IsAuthenticated()]'''
    
    # filtering and Sorting tasks
    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.filter(assigned_to=user)
        
        status = self.request.query_params.get('status')
        priority = self.request.query_params.get('priority')
        sort_tasks = self.request.query_params.get('ordering')
        search_task = self.request.query_params.get('search')
        
        if status:
            queryset = queryset.filter(status=status)
            
        if priority:
            queryset = queryset.filter(priority=priority)
        
        if sort_tasks:
            queryset = queryset.order_by(sort_tasks)
        
        if search_task:
            queryset = queryset.filter(title__icontains=search_task)
            
        return queryset

class TaskDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    # specific permission that only AdminUser can delete task
    '''def get_permissions(self):
        if self.request.method == 'DELETE':
            return [IsAdminUser()]
        return [IsAuthenticated()]'''
    
    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.filter(assigned_to=user)
        
        return queryset