from django.urls import path
from account.views import UserRegisterView, LoginView, Home

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-create'),
    path('login/', LoginView.as_view(), name='login'),
    path('index/', Home.as_view(), name='index'),
]
