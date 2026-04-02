from django.db import models

# Create your models here.

class users(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    confirmPassword = models.CharField(max_length=128)

    def __str__(self):
        return self.username
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)  
    message = models.TextField()

    def __str__(self):
        return self.name
    
class ClothingProduct(models.Model):
    CATEGORY_CHOICES = [
        ('men', 'Men'),
        ('women', 'Women'),
        ('kids', 'Kids'),
    ]

    CLOTH_TYPE_CHOICES = [
        ('shirt', 'Shirt'),
        ('tshirt', 'T-Shirt'),
        ('jeans', 'Jeans'),
        ('hoodie', 'Hoodie'),
        ('jacket', 'Jacket'),
        ('dress', 'Dress'),
        ('kurta', 'Kurta'),
    ]

    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Double XL'),
    ]

    name = models.CharField(max_length=200)
    product_code = models.CharField(max_length=100, unique=True)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='men'
    )

    cloth_type = models.CharField(
        max_length=50,
        choices=CLOTH_TYPE_CHOICES
    )

    brand = models.CharField(max_length=100)

    description = models.TextField()

    price = models.DecimalField(max_digits=10, decimal_places=2)

    discount_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    color = models.CharField(max_length=50)

    size = models.CharField(
        max_length=10,
        choices=SIZE_CHOICES,
        default='M'
    )

    fabric = models.CharField(max_length=100)

    fit_type = models.CharField(
        max_length=50,
        default='Regular Fit'
    )

    sleeve_type = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    stock = models.PositiveIntegerField(default=0)

    image = models.ImageField(upload_to='clothing/')
    image_2 = models.ImageField(
        upload_to='clothing/',
        blank=True,
        null=True
    )
    image_3 = models.ImageField(
        upload_to='clothing/',
        blank=True,
        null=True
    )

    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=5.0
    )

    reviews = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name