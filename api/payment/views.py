from braintree.configuration import Configuration
from braintree.environment import Environment
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.apps import get_user_model
from django.views.decorators.csrf import csrf_exempt

import braintree

gateway = braintree.BraintreeGateway(
    Configuration(
        Environment.Sandbox,
        merchant_id="jqtyhxxwfwqgz66w",
        public_key="krkv8p6zjyjsvkxn",
        private_key="e22b7712d09137e2abd1331c6dd6b56a"
    )
)


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
def generate_token(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({"error": "Invalid session"})

    return JsonResponse({"client_token": gateway.client_token.generate(), "success": True})


@csrf_exempt
def process_payment(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({"error": "Invalid session"})

    nonce_from_client = request.POST['payment_method_nonce']
    amount_from_client = request.POST['amount']

    result = gateway.transaction.sale({
        "amount": amount_from_client,
        "payment_method_nonce": nonce_from_client,
        "options": {
            "submit_for_settlement": True
        }
    })

    print(result)
    if result.is_success:
        return JsonResponse({
            "success": result.is_success,
            "transaction": {
                "id": result.transaction.id,
                "amount": result.transaction.amount
            }
        })
    else:
        return JsonResponse({"error": True, "success": False})
