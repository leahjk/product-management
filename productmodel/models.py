from cmath import atan
from unicodedata import name
#from unittest.util import _MAX_LENGTH
from django.db import models


class product(models.Model):
    name=models.CharField(max_length=255, blank=True)
    sku=models.CharField(max_length=100,unique=True, blank=True)
    description=models.TextField(blank=True)
    quantity=models.PositiveIntegerField(blank=True,null=True)
    price =models.DecimalField(max_digits= 20,decimal_places=2,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
            verbose_name = ("product")
            verbose_name_plural = ("products")
            ordering = ['-updated_at']

            
    def __str__(self):
                return self.name        



        
