from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
USER = settings.AUTH_USER_MODEL


class CategoryModel(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

class ProductsModel(models.Model):
    user = models.ForeignKey(USER, on_delete=models.CASCADE, default=1)    
    category = models.ForeignKey(
        CategoryModel, on_delete=models.SET_NULL, null=True, blank=True)
    product_name = models.CharField(max_length=30, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    image = models.ImageField(upload_to="product/images" , default="default/product.png" )
    description = models.TextField()
    created_date  = models.DateField(auto_now=True)
    
    def get_absolute_url(self):
        url = reverse("product:product_create", kwargs={"pk": self.id})    




    def __str__(self):
        return self.user.username