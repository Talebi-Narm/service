from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from common.models import BaseModel, EmailField


class Gender(models.IntegerChoices):
    MALE = 0, "Male"
    FEMALE = 1, "Female"
    NONBINARY = 2, "Non-Binary"
    RATHERNOTTOSAY = 3, "Rather not to say!"


def upload_to(instance, filename):
    filename = str(instance.pk) + '.' + filename.split('.')[-1]
    return 'images/{filename}'.format(filename=filename)


class User(AbstractUser, BaseModel):
    email = EmailField(max_length=255, unique=True)

    gender = models.IntegerField(choices=Gender.choices, null=True, default=3)

    calendar_id = models.CharField(max_length=200, blank=True, null=True)
    calendar_token = models.TextField(max_length=1000, blank=True, null=True)

    about = models.TextField(max_length=500, blank=True)
    avatar_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    wallet_charge = models.IntegerField(default=0)

    # check this
    phone_regex = RegexValidator(regex=r'^(\+98|0)9\d{9}$')
    phone_number = models.CharField(validators=[phone_regex], max_length=13, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.get_username()


class UserAddress(BaseModel):
    owner = models.ForeignKey("User", on_delete=models.CASCADE)
    address = models.TextField()
    label = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'User Address'
        verbose_name_plural = 'User Addresses'
        unique_together = (('owner', 'address'), ('owner', 'label'))

    def __str__(self):
        return self.address
