from turtle import position
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from datetime import datetime
# Create your models here.
class UserAccessManager(BaseUserManager):

    # Manager to setup users

    def create_user(self, email, name, password=None):
        # Create a New User Profile
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user  = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff= True
        user.save(using=self._db)

        return user
class UserAccess(AbstractBaseUser, PermissionsMixin):
    # User access for API
    email     = models.EmailField(max_length=255, unique=True)
    name      = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff  = models.BooleanField(default=False)

    objects = UserAccessManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        # Get User Name
        return self.name
        # Get Short Name
    def get_short_name(self):
        return self.name

    def __str__(self):
        # Return User String
        return self.email
class Team(models.Model):
    # Teams of Soccer World Cup
    teamName = models.CharField(max_length=15)
    flag     = models.CharField(max_length=15)
    shield   = models.CharField(max_length=15)

    def __str__(self):
        return self.teamName

class Player(models.Model):
    # Players model of World Cup
    teamName_id   = models.ForeignKey(Team, on_delete=models.CASCADE, blank = True, null = True)
    playerPicture = models.CharField(max_length=20)
    name          = models.CharField(max_length=20)
    lastName      = models.CharField(max_length=20)
    birthDate     = models.DateField()
    position      = models.CharField(max_length=20)
    shirtNumber   = models.FloatField()
    is_starting   = models.BooleanField()

    @property
    def age(self):
        return int((datetime.now() - self.instance.birthDate).days / 365.25)

    def __str__(self):
        return self.name


class Staff(models.Model):
    name          = models.CharField(max_length=20)
    lastName      = models.CharField(max_length=20)
    birthDate     = models.DateField()
    lastName      = models.CharField(max_length=20)
    nationality   = models.CharField(max_length=20)
    Role          = models.CharField(max_length=20)

    def __str__(self):
        return self.name