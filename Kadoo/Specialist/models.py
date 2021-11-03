from django.db import models
from django.db.models.query import EmptyQuerySet, QuerySet
from django.core.validators import RegexValidator

from Users.models import NewUser

class SpecialistManager(models.Manager):
    def creat(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=NewUser.Types.SPECIALIST)

class Specialist(NewUser):
    base_type = NewUser.Types.SPECIALIST
    objects = SpecialistManager()

    @property
    def more(self):
        return self.SpecilistFields

    class Meta:
        proxy = True


class SpecialistFieldsManager(models.Manager):
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

class SpecilistFields(models.Model):

    class Degrees(models.TextChoices):
        ASSOCIATE = "Associate", "Associate"
        BACHELER = "Bachelor", "Bachelor"
        MASTER = "Master", "Master"
        DOCTORAL = "Doctoral", "Doctoral"

    user = models.OneToOneField(Specialist, on_delete=models.CASCADE, related_name='specialist_user')
    id_code = models.CharField('id_code', max_length=150, blank=True)
    birth_date = models.DateField('birth_date', blank=True, null=True)
    degree = models.CharField('degree', max_length=50, choices=Degrees.choices, null=True, blank=True)
    major = models.CharField('id_code', max_length=150, blank=True) 
    phone_regex = RegexValidator(regex=r'^(\+\d{1,2}\s?)?1?\-?\.?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$', message="Phone number must be entered in the format: '+## ### ### ####'. Up to 10 digits allowed.")
    phone_number = models.CharField('phone_number', validators=[phone_regex], max_length=17, blank=True)
    about = models.TextField('about', max_length=500, blank=True)
    address = models.TextField('address', max_length=500, blank=True)
    is_online = models.BooleanField(default=True)
    rate = models.IntegerField('rate', default=0)
    #Ticket

    objects = SpecialistFieldsManager()

    def __str__(self):
        return str(self.user)