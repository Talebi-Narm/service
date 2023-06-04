import uuid

from django.db import models
from django.utils import timezone


class EmailField(models.EmailField):
    def get_prep_value(self, value):
        value = super(EmailField, self).get_prep_value(value)
        if value is not None:
            value = value.strip().lower()
        return value


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.is_deleted is True:
            self.is_active = False
        super(BaseModel, self).save(*args, **kwargs)

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()


class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class PlantBookmark(BaseModel):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    Plant = models.ForeignKey("store.Plant", on_delete=models.CASCADE)


class ToolBookmark(BaseModel):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    Tool = models.ForeignKey("store.Tool", on_delete=models.CASCADE)
