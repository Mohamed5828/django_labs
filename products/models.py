from django.db import models

# Category Model
class Category(models.Model):
    cat_name = models.CharField(max_length=100)

    def __str__(self):
        return self.cat_name

# Product Model
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='photos/%y/%m/%d', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return f"{self.name} : {self.active}"

    class Meta:
        verbose_name = "My Product"
        ordering = ['-name']

# Payment Model
class Payment(models.Model):
    order_type = models.CharField(max_length=100)
    def __str__(self):
        return self.order_type

# Order Model with Many-to-Many relationship
class Order(models.Model):
    order_name = models.CharField(max_length=100)
    order_payment_method = models.OneToOneField(Payment, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    order_id = models.CharField(max_length=100)

    def __str__(self):
        return self.order_name
