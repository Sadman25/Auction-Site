from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateField
# Create your models here.

class status (models.Model):
    status = models.CharField(max_length=20, unique=True)
    

class product(models.Model):
    product_name= models.CharField(max_length=50, blank=False)
    product_description=models.CharField(max_length=500,null=False, blank=False)
    cover_photo=models.ImageField(null=False, blank=False,upload_to='product_cover_photos/')
    starting_bid = models.CharField(max_length=10, null=False, blank=False)
    deadline = models.DateTimeField()
    owner = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    product_status = models.ForeignKey(status, null=True, on_delete= models.SET_NULL)

    def __str__(self) -> str:
        return self.product_name + self.owner

class images(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='product_photos/',blank=False, null=False)

    def __str__(self):
        return self.product.product_name + self.product.product_owner
