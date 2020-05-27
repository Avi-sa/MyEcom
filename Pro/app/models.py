from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=120,blank=False,null=False)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=100,decimal_places=2,default ='29.99')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('product',kwargs=['slug':slug]);



# Create your models here.
