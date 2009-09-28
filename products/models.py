from django.db import models

class Product(models.Model):
    """ Model for the products sold on FOA
    """

    title = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image_1 = models.ImageField(upload_to="images", null=True, blank=True)
    image_2 = models.ImageField(upload_to="images", null=True, blank=True)
    image_3 = models.ImageField(upload_to="images", null=True, blank=True)
    image_4 = models.ImageField(upload_to="images", null=True, blank=True)

    def __unicode__(self):
        return self.title

    def get_product_sibling(self, movement):
        all_products = [ p for p in Product.objects.all() ]
        current_index = all_products.index(self)
        previous_index = current_index - 1 if current_index > 1 else 0
        count_of_products = len(all_products)
        next_index = current_index + 1 if current_index < count_of_products - 1 else count_of_products - 1
        
        if movement == "first":
            product = all_products[0]
        elif movement == "previous":
            product = all_products[previous_index]
        elif movement == "next":
            product = all_products[next_index]
        elif movement == "last":
            product = all_products[count_of_products - 1 ]

        return product

    def get_absolute_url(self):
        return "/products/%s/" % self.slug
            
