from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AddCategory(models.Model):
    category_name = models.CharField(max_length=100, unique=True),
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='category')
    created_on = models.DateTimeField(auto_now_add=True)

