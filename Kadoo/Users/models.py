from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, last_name, password, **other_fields):
        #other_fields.setdefault('type', )
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        email = self.normalize_email(email)
        if not email:
            raise ValueError('You must provide an email address')
        if not user_name:
            raise ValueError('You must provide an user name')
        if not first_name:
            raise ValueError('You must provide an first name')
        if not last_name:
            raise ValueError('You must provide an last name')
        user = self.model(email=email, type=NewUser.Types.ADMIN, user_name=user_name,
                          first_name=first_name, last_name=last_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, type, email, user_name, first_name, last_name, password, **other_fields):
        if not email:
            raise ValueError('You must provide an email address')
        if not user_name:
            raise ValueError('You must provide an user name')
        if not first_name:
            raise ValueError('You must provide an first name')
        if not last_name:
            raise ValueError('You must provide an last name')

        email = self.normalize_email(email)
        user = self.model(type= type, email=email, user_name=user_name,
                          first_name=first_name, last_name=last_name, **other_fields)
        user.set_password(password)
        user.save()
        return user




class NewUser(AbstractBaseUser, PermissionsMixin):

    class Types(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        SPECIALIST = "SPECIALIST", "Specialist"
        MEMBER = "MEMBER", "Member"

    base_type = Types.MEMBER
    type = models.CharField('type', max_length=50, choices=Types.choices)
    email = models.EmailField('email address', unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    #image
    is_active = models.BooleanField(default=True)
    about = models.TextField('about', max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name', 'last_name']

    def __str__(self):
        return self.user_name

#--- Member Def
class MemberManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=NewUser.Types.MEMBER)

class Member(NewUser):
    base_type = NewUser.Types.MEMBER
    objects = MemberManager()

    class Meta:
        proxy = True

class MemberFields(models.Model):
    user = models.OneToOneField(NewUser, on_delete=models.CASCADE)
    credit_value = models.IntegerField(default=0)
    #Card

#--- Specialist Def
class SpecialistManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=NewUser.Types.SPECIALIST)

class Specialist(NewUser):
    base_type = NewUser.Types.SPECIALIST
    objects = SpecialistManager()

    @property
    def more(self):
        return self.SpecilistFields

    class Meta:
        proxy = True

class SpecilistFields(models.Model):
    user = models.OneToOneField(NewUser, on_delete=models.CASCADE)
    #Ticket
