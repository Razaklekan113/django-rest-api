from rest_framework import mixins, viewsets

from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    get => list => queryset
    get => retrieve => Product Instances Detail View
    post => create New Instances
    put => update New Instances
    patch => patial Update
    delete => destroy
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' # default

class ProductGenericViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet):
    """
    get => list => queryset
    get => retrieve => Product Instances Detail View

    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' # default

# product_list_view = ProductGenericViewSet.as_view({'get':'list'})
# product_detail_view = ProductGenericViewSet.as_view({'get':'retrieve'})




