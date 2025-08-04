from django.db import models
from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name) 
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self): 
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    title = models.CharField(max_length=128)
    url = models.URLField()
    
    def __str__(self): 
        return self.title
    
from django.db import models

class Enquiry(models.Model):
    PRODUCT_CHOICES = [
        ('machinery', 'Machinery'),
        ('steel', 'Steel'),
        ('tools', 'Tools'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=128, verbose_name="Full Name")
    company_name = models.CharField(max_length=128, verbose_name="Company Name")
    email = models.EmailField(verbose_name="Email Address")
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number")
    enquiry = models.TextField(blank=True, null=True, verbose_name="Enquiry Details")
    product_choice = models.CharField(max_length=20, choices=PRODUCT_CHOICES, verbose_name="Product Interested In")

    def __str__(self):
        return f"{self.name} - {self.product_choice}"

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    description = models.TextField()
    overview = models.TextField()
    specifications = models.TextField()
    countries_sold = models.CharField(max_length=255)
    is_new = models.BooleanField(default=False)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    catalog_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Building(models.Model):
    name = models.CharField(max_length=200)
    series = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)  # Add this if missing
    photo = models.ImageField(upload_to='UenoBuildings/', blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    
