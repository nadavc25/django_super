from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    img = models.ImageField(upload_to='static/')

    def __str__(self):
        return self.description

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    price = models.FloatField()
    img = models.ImageField(upload_to='static/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.user.username} on {self.order_date}"

class OrderDetails(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Order details for {self.product.description} in order by {self.order.user.username}"

    def get_product_total(self):
        return self.product.price * self.quantity

    def get_order_subtotal(self):
        order_details = OrderDetails.objects.filter(order=self.order)
        subtotal = sum(detail.get_product_total() for detail in order_details)
        return subtotal
    
