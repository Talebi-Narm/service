# from django.db import models
# from django.db.models.query import EmptyQuerySet, QuerySet
# from django.core.validators import RegexValidator
#
# from user.models import NewUser
#
# class SpecialistManager(models.Manager):
#     def get_empty_query_set(self):
#         return self.EmptyQuerySet(self.model, self._db)
#
#     def get_query_set(self, *args, **kwargs):
#         return super().get_queryset(*args, **kwargs).filter(type=NewUser.Types.SPECIALIST)
#
#     def get_or_create(self, *args, **kwargs):
#         return self.get_query_set().get_or_create(*args, **kwargs)
#
#     def creat(self, *args, **kwargs):
#         return super().get_queryset(*args, **kwargs).filter(type=NewUser.Types.SPECIALIST)
#
# class Specialist(NewUser):
#     base_type = NewUser.Types.SPECIALIST
#     objects = SpecialistManager()
#
#     @property
#     def more(self):
#         return self.SpecilistFields
#
#     class Meta:
#         proxy = True
#
#
# class SpecialistFieldsManager(models.Manager):
#     EmptyQuerySet = EmptyQuerySet
#     QuerySet = QuerySet
#
#     def get_empty_query_set(self):
#         return self.EmptyQuerySet(self.model, self._db)
#
#     def get_query_set(self):
#         return self.QuerySet(self.model, self._db)
#
#     def get_or_create(self, *args, **kwargs):
#         return self.get_query_set().get_or_create(*args, **kwargs)
#
#     def create(self, *args, **kwargs):
#         return self.get_query_set().create(*args, **kwargs)
#
