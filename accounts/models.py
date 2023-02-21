# accounts/models.py
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        """
        Function create_user creates user account
        """
        if not email:
            raise ValueError('Email Adress is mandatory')
        if not username:
            raise ValueError('Username is mandatory')
        if not password:
            raise ValueError('Password is mandatory')

        user = self.model(
            username=username,
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        """
        Function create_superuser creates superuser account
        """
        user = self.create_user(username, email, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    username = models.CharField(
        max_length=30,
        validators=[
            RegexValidator(
                regex=USERNAME_REGEX,
                message='User must be alpha-numeric',
                code='invalid username'
            )],
        unique=True
    )
    email = models.EmailField(
        max_length=75,
        unique=True,
        verbose_name='email address'
    )
    firstname = models.CharField(
        max_length=75,
        blank=True
    )
    lastname = models.CharField(
        max_length=75,
        blank=True
    )
    fullname = models.CharField(
        max_length=151,
        blank=True
    )
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_on = models.DateTimeField(auto_now_add=True, null=True)
    modified_on = models.DateTimeField(auto_now=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return self.fullname

    # functions has_module_perms and has_perm
    # is required to view django admin panel
    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True
