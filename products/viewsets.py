from rest_framework import viewsets, mixins


from .models import Products
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"


class ProductGenericViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
