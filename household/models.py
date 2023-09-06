from django.db import models

# Create your models here.
class Household(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    # Should I add here the user_id as foreign key? After creating teh userextend app
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

