from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)


class UserManager(BaseUserManager):
    def create_user(self, email, username, is_staff=False, is_admin=False, is_active=True, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        if not username:
            raise ValueError('Users must have a username')

        if not password:
            raise ValueError("A user must have a Password")

        user_obj = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user_obj.set_password(password)
        user_obj.is_staff = is_staff
        user_obj.is_admin = is_admin
        user_obj.is_active = is_active
        user_obj.save(using=self._db)
        return user_obj

    # def create_staffuser(self, email, username, password=None):
    #     user = self.create_user(
    #         email,
    #         username,
    #         password=password,
    #         is_staff=True
    #     )
    #     return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email,
            username,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(max_length=254, unique=True)
    is_active = models.BooleanField(default=True)  # can login
    is_staff = models.BooleanField(default=False)  # staff but non superuser
    is_admin = models.BooleanField(default=False)  # sueruser
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    # username and password fields are required by default
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return True
    
    def has_module_perms(self,app_label):
        return True

    # @property
    # def is_staff(self):
    #     return self.is_staff

    # @property
    # def is_admin(self):
    #     return self.is_admin

    # @property
    # def is_active(self):
    #     return self.is_active

    