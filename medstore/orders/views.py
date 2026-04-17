import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Cart
from products.models import Product

@csrf_exempt
def add_to_cart(request):
    if request.method == "POST":
        data = json.loads(request.body)

        product = Product.objects.get(id=data['product_id'])

        cart_item, created = Cart.objects.get_or_create(
            user=request.user,
            product=product
        )

        if not created:
            cart_item.quantity += data.get('quantity', 1)
            cart_item.save()

        return JsonResponse({"message": "Added to cart"})
    
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)

    data = []
    for item in cart_items:
        data.append({
            "product": item.product.name,
            "price": item.product.price,
            "quantity": item.quantity
        })

    return JsonResponse(data, safe=False)
