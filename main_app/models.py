from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Merchant(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	photo = models.ImageField(upload_to='image/',blank=True, null=True)
	#mobile = models.CharField(max_length=11, blank=True, null=True)

	def __str__(self):
		return self.user.username

class Order(models.Model):
    STATUS_CHOICE = (
        ('f', 'Fragile'),
        ('l', 'Liquid'),
    )
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    product_type = models.CharField(max_length=10, choices=STATUS_CHOICE,default='p')
    created_date = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=120,blank=True, null=True)
    price = models.DecimalField(blank=True, null=True,max_digits=10, decimal_places=2)


    def __str__(self):
        return self.merchant.user.username
