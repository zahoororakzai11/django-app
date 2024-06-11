from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Products
def validate_title(value):
    qs = Products.objects.filter(title__iexact=value)
    if qs.exists():
        raise serializers.ValidationError(f'{value} is already a product name')
    return value
