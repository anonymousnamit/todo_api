from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    def create_user(self, username, name, password=None):

        if not username:
            raise ValueError('Username not provided')

        user = self.model(username=username, name=name)
        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, username, name, password):

        user = self.create_user(username, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name',]

    def __str___(self):
        return self.username



class TodoStuffs(models.Model):
    user = models.ForeignKey(UserProfile, to_field=UserProfile.USERNAME_FIELD, on_delete=models.CASCADE)
    todo_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.todo_text
