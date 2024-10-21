from django.urls import path
from account.views import Home

urlpatterns = [
    path('index/', Home.as_view()),
]
