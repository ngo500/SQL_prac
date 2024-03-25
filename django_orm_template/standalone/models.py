from django.db import models

# Test model
# name as CharField
class Test(models.Model):
    name = models.CharField(max_length=30)
  
