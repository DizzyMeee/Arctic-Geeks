from django.db import models

# Create your models here.
class TagComponent(models.Model): # tag component like Processor, Motherboard, etc.
    name = models.CharField(max_length=100)

class Component(models.Model):
    title = models.CharField(max_length=150)
    TagComponent = models.ForeignKey(TagComponent, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10)
