from rest_framework import viewsets
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

from .serializers import OrderSerializer
from .models import Order
from django.views.decorators.csrf import csrf_exempt


def validate_user_session(id, token):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False
    except UserModel.DoesNotExist:
        return False

@csrf_exempt
def add(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({"error": "Please log in", "code":"401"})
    if request.method == "POST":
        user_id = id
        transaction_id = request.POST['transaction_id']
        amount = request.POST['amount']
        products = request.POST['products']

        total_products = len(products.split(",")[:-1])

        UserModel = get_user_model()

        try:
            user = UserModel.objects.get(pk=user_id)

        except UserModel.DoesNotExist:
            return JsonResponse({"error":"User does not exist"})

        order = Order(user, product_names=products, total_products=total_products, total_amount=amount, transaction_id=transaction_id)
        order.save()
        return JsonResponse({"success":True, 'error': False, 'msg':'Order placed successfully'})

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer