from django.db import models

class Product(models.Model):
    """ Model for the products sold on FOA
    """

    title = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __unicode__(self):
        return self.title

