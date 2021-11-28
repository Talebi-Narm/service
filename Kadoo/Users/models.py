from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models.query import EmptyQuerySet, QuerySet
from django.core.validators import RegexValidator


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
            raise ValueError('You must provide a user name')
        if not first_name:
            raise ValueError('You must provide a first name')
        if not last_name:
            raise ValueError('You must provide a last name')
        
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
    type = models.CharField('type', max_length=50, choices=Types.choices, default=base_type)
    email = models.EmailField('email address', unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    calendarID = models.CharField(max_length=150, blank=True, null=True)
    creds = models.TextField(max_length=500, blank=True, null=True)
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

class MemberFieldsManager(models.Manager):
    EmptyQuerySet = EmptyQuerySet
    QuerySet = QuerySet

    def get_empty_query_set(self):
        return self.EmptyQuerySet(self.model, self._db)

    def get_query_set(self):
        return self.QuerySet(self.model, self._db)

    def get_or_create(self, *args, **kwargs):
        return self.get_query_set().get_or_create(*args, **kwargs)

    def create(self, *args, **kwargs):
        return self.get_query_set().create(*args, **kwargs)

class MemberFields(models.Model):
    user = models.OneToOneField(NewUser, on_delete=models.CASCADE, related_name='user')
    credit_value = models.IntegerField('credit', default=0)
    address = models.TextField('address', max_length=500, blank=True)
    phone_regex = RegexValidator(regex=r'^(\+\d{1,2}\s?)?1?\-?\.?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$', message="Phone number must be entered in the format: '+## ### ### ####'. Up to 10 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    objects = MemberFieldsManager()

    def __str__(self):
        return str(self.user)

