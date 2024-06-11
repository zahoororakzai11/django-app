from rest_framework import serializers
from rest_framework import reverse
from .models import Products
from . import validators  # validators from products/validators.py

from api.serializers import UserPublicSerializer


class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source="user", read_only=True)
    my_discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", lookup_field="pk"
    )
    email = serializers.EmailField(read_only=True)
    title = serializers.CharField(
        validators=[validators.validate_title, validators.UniqueValidator]
    )

    class Meta:
        model = Products

        fields = [
            "email",
            "owner",
            "title",
            "url",
            "pk",
            "title",
            "email",
            "content",
            "price",
            "sale_price",
            "my_discount",
        ]

    def get_my_discount(self, obj):
        if not hasattr(obj, "id"):
            return None
        if not isinstance(obj, Products):
            return None
        return obj.get_discount()
