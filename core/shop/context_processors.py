# shop/context_processors.py

from .models import ShopInfo

def shop_info(request):
    try:
        # Retrieve the ShopInfo object
        shop_info = ShopInfo.objects.first()
    except ShopInfo.DoesNotExist:
        shop_info = None
    
    return {
        'shop_info': shop_info
    }
