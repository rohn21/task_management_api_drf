from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):
    
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save a User with Given email, name and password.
        """
        if not email:
            raise ValueError("User must have an Email address.")
        
        user = self.model(email=self.normalize_email(email), **extra_fields)
        
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and save a superuser with given email, name and password.
        """        
        user = self.create_user(email, password, **extra_fields)
        user.is_admin = True
        user.save(using=self.db)
        return user
    
class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='Email',
                              max_length=254,
                              unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return self.first_name + self.last_name
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return self.is_admin
    
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_lable`?"
        return True
    
    @property
    def is_staff(self):
        return self.is_admin