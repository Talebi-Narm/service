from django.forms import ModelForm
from .models import Plant, Tool, Tag

class PlantForm(ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'

class ToolForm(ModelForm):
    class Meta:
        model = Tool
        fields = '__all__'

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'