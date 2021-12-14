from django.db import models

# Create your models here.
from products.models import GPU

class Build(models.Model):
    gpu = models.ForeignKey(GPU, null=True, on_delete=models.DO_NOTHING)