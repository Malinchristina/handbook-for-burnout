from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# Create your models here.
class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    comment = models.TextField()
    rating = models.IntegerField()
    activity_id = models.ForeignKey('activities.AddActivity', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    def clean(self):
        # Check that the rating is between 1 and 5
        if self.rating < 1 or self.rating > 5:
            raise ValidationError({'rating': 'Rating must be between 1 and 5.'})

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
            super().save(update_fields=['comment', 'rating'], *args, **kwargs)
