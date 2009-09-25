from django.db import models

class Product(models.Model):
    """ Model for the products sold on FOA
    """

    title = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image_1 = models.ImageField(upload_to="images", null=True, blank=True)
    image_2 = models.ImageField(upload_to="images", null=True, blank=True)
    image_3 = models.ImageField(upload_to="images", null=True, blank=True)
    image_4 = models.ImageField(upload_to="images", null=True, blank=True)

    def __unicode__(self):
        return self.title

