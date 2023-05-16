from django.db import models

class Product(models.Model):
    options_category = (
        ('undefined', 'Undefined'),
        ('shampoo', 'Shampoo'),
        ('conditioner', 'Conditioner'),
        ('oil', 'Oil')
    )

    name = models.CharField(max_length=100)
    description = models.TextField()
    price_for_selling = models.DecimalField(max_digits=8, decimal_places=2)
    price_for_purchase = models.DecimalField(max_digits=8, decimal_places=2)
    percentage_gain = models.IntegerField()
    #imagen = models.ImageField(upload_to='productos/')
    category = models.CharField(max_length=50, choices=options_category, default='undefined')

