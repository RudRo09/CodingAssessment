from django.db import models

# Create your models here.
class Sales(models.Model):
    order_id = models.TextField(null=True)
    order_date = models.DateField(null=True)
    ship_date = models.DateField(null=True)
    customer_id = models.TextField(null=True)
    customer_name = models.TextField(null=True)
    segment = models.TextField(null=True)
    country = models.TextField(null=True)
    city = models.TextField(null=True)
    state = models.TextField(null=True)
    postal_code = models.TextField(null=True)
    region = models.TextField(null=True)
    product_id = models.TextField(null=True)
    category = models.TextField(null=True)
    sub_category = models.TextField(null=True)
    product_name = models.TextField(null=True)
    sales = models.DecimalField(null=True, max_digits=10, decimal_places=2)

    def __str__(self):
        return self.order_id



