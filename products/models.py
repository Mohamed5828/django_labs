from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=100 ,decimal_places=2)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='photos/%y/%m/%d', blank=True)

    def __str__(self) -> str:
        return f"{self.name}    :   {self.active}"
    class Meta:
        verbose_name = "My Product"
        ordering = ['-name']

class Payment(models.Model):
    order_type = models.CharField(max_length=100)
    order_id = models.IntegerField(max_length=100)

class Order(models.Model):
    order_name = models.CharField(max_length=100)
    order_payment_method = models.OneToOneField(Payment, on_delete=models.CASCADE )