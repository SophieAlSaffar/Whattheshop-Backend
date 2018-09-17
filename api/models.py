from django.db import models

class Product(models.Model):
    # id = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    image = models.ImageField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return self.name