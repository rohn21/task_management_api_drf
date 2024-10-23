from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status 
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from account.models import User
from account.serializers import UserRegisterSerializer, UserLoginSerializer


class UserRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
class LoginView(TokenObtainPairView):
    serializer_class = UserLoginSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        access_token = refresh.access_token
        response = {
            'refresh': str(refresh),
            'access': str(access_token),
            'user': serializer.data,
        }
                
        return Response(response, status=status.HTTP_200_OK)
    
