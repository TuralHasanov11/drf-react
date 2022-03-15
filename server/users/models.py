from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class AccounthManager(BaseUserManager):
    
    def create_user(self, email, username, first_name, last_name, password=None, **kwargs):
        
        if not email:
            raise ValueError("Email is required")

        if not username:
            raise ValueError("Username is required")

        user = self.model(
            email=self.normalize_email(email),
            username = username,
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, username, first_name, last_name, password, **kwargs):
        user = self.create_user(
            email=self.normalize_email(email),
            username = username,
            first_name=first_name,
            last_name=last_name,
            password = password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser= True
        user.save(using=self._db)
        return user
        

class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', unique=True)
    username= models.CharField(max_length=50, unique=True)
    first_name= models.CharField(max_length=50, blank=True)
    last_name= models.CharField(max_length=50, blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    objects = AccounthManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.username


