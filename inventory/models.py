from django.db import models

class  Inventory_Items(models.Model):
    name = models.CharField(max_length=255, unique=True)  
    description = models.TextField()  
    unit_price = models.DecimalField(max_digits=10, decimal_places=2) 
    quantity = models.PositiveIntegerField()  
    category = models.CharField(max_length=100)  
    supplier = models.CharField(max_length=100)  

    def __str__(self):
        return self.name