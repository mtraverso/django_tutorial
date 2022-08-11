from rest_framework.serializers import HyperlinkedModelSerializer

from api.order.models import Order


class OrderSerializer(HyperlinkedModelSerializer):
    class Meta:
        model= Order
        fields = ['user', 'product_names', 'total_products', 'transaction_id', 'total_amount']