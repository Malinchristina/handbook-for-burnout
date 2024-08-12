from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# Create your models here.
class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    comment = models.TextField()
    activity_pk = models.ForeignKey('activities.AddActivity', on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.author} on {self.created_on}'
