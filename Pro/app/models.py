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

    class Meta:
        unique_together = ('title','slug')
    # def get_absolute_url(self):
    #     return reverse('product',kwargs=['slug':slug]);

class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/images')
    featured = models.BooleanField(default=True)
    thumbnail = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)

    def __str__(self):
        return self.product.title

# Create your models here.
