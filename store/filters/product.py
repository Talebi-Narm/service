from django_filters import FilterSet, filters

from store.models import Plant, Tool


class PlantFilter(FilterSet):
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Plant
        fields = ['environment', 'water', 'light', 'growth_rate', 'tags']


class ToolFilter(FilterSet):
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Tool
        fields = ['tags']
