from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.city

class History(models.Model):
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.message

# class CountryInfo(models.Model):
#     country_code = models.CharField(max_length=2, null=False)
#     country_name = models.CharField(max_length=70)
#     country_alpha3_code = models.CharField(max_length=3)
#     country_numeric_code = models.IntegerField()
#     capital = models.CharField(max_length=50)
#     country_demonym = models.CharField(max_length=100)
#     idd_code = models.CharField(max_length=6)
#     currency_code = models.CharField(max_length=3)
#     currency_name = models.CharField(max_length=50)
#     currency_symbol = models.CharField(max_length=10)
#     lang_name = models.CharField(max_length=50)

