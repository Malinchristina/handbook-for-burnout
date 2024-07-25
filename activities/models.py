from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

LEVEL = ((0, "Level 1"), (1, "Level 2"), (2, "Level 3"),)

# Create your models here.

class AddActivity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    activity_name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey('categories.AddCategory', on_delete=models.CASCADE)
    level= models.IntegerField(choices=LEVEL,)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    url_link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.activity_name

    def clean(self):
        # Check for uniqueness of activity_name, excluding the current instance in case of update
        if AddActivity.objects.exclude(pk=self.pk).filter(activity_name=self.activity_name).exists():
            raise ValidationError({'activity_name': 'An activity with this name already exists.'})

    def save(self, *args, **kwargs):
        # Call the clean method to validate the instance before saving
        self.clean()
        super().save(*args, **kwargs)
        # Determine whether this is a new record or an update
        if self._state.adding:
            # This is a new record; proceed with normal save
            super().save(*args, **kwargs)
        else:
            # This is an update; skip the clean method since it's already been called
            super().save(update_fields=['activity_name'], *args, **kwargs)
