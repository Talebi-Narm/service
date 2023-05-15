from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from common.models import BaseModel, EmailField


class Gender(models.IntegerChoices):
    MALE = 0, "Male"
    FEMALE = 1, "Female"
    NONBINARY = 2, "Non-Binary"
    RATHERNOTTOSAY = 3, "Rather not to say!"


class User(AbstractUser, BaseModel):
    email = EmailField(max_length=255, unique=True)

    gender = models.IntegerField(choices=Gender.choices)

    calendar_id = models.CharField(max_length=200, blank=True, null=True)
    calendar_token = models.TextField(max_length=1000, blank=True, null=True)

    about = models.TextField(max_length=500, blank=True)

    wallet_charge = models.IntegerField(default=0)

    # check this
    phone_regex = RegexValidator(regex=r'^(\+98?)?{?(0?9[0-9]{9,9}}?)$')
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


class Degree(models.IntegerChoices):
    ASSOCIATE = 0, "Associate"
    BACHELOR = 1, "Bachelor"
    MASTER = 2, "Master"
    DOCTORAL = 3, "Doctoral"


class Specialist(User):
    birth_date = models.DateField(blank=True, null=True)
    degree = models.IntegerField(choices=Degree.choices, null=True, blank=True)
    major = models.CharField(max_length=150, blank=True)
    rate = models.IntegerField('rate', default=3)

    def __str__(self):
        return str(self.username)
