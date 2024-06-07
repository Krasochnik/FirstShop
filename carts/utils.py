from carts.models import Cart

def get_user_carts(r):
    if r.user.is_authenticated:
        return Cart.objects.filter(user=r.user).select_related('product')
    
    if not r.session:
        r.session.create()
    return Cart.objects.filter(session=r.session).select_related('product')
