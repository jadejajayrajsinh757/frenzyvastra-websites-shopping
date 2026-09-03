from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_title = models.CharField(max_length=200)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    available_qty = models.IntegerField()
    product_img = models.ImageField(upload_to='products/')
