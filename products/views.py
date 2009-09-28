from django.http import HttpResponseRedirect

from foa.products.models import Product

# Create your views here.

def move_to_product(request, slug, movement):
    product = Product.objects.get(slug=slug)
    redirect = product.get_product_sibling(movement)
    return HttpResponseRedirect(redirect.get_absolute_url())
