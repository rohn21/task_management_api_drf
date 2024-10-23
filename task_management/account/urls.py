from django.urls import path
from account.views import UserRegisterView, LoginView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-create'),
    path('login/', LoginView.as_view(), name='login'),
]
