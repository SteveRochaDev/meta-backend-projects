from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    menu_description = models.TextField(max_length=1000, default="Delicious item")

    def __str__(self):
        return self.name