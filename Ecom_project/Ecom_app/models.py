from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    desc=models.TextField()
    image = models.ImageField(upload_to='category',blank=True)
    class Meta:
        ordering=('name' ,)
        verbose_name='Category'
        verbose_name_plural='Categories'

    def __str__(self):
        return '{}' .format(self.name)

    def get_url(self):
        return reverse('Ecom_app:products_by_category',args=[self.slug])


class Product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    desc = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product',blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def get_url(self):
        return reverse('Ecom_app:prodCatDetail',args=[self.category.slug,self.slug])

    class Meta:
        ordering=('name' ,)
        verbose_name='Product'
        verbose_name_plural='Products'

    def __str__(self):
        return '{}' .format(self.name)




