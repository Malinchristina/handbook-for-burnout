from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.


class AddCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

    def clean(self):
        # Check if a category with the same name already exists
        if AddCategory.objects.exclude(pk=self.pk).filter(
                category_name=self.category_name).exists():
            raise ValidationError(
                {'category_name': 'A category with this name already exists.'})

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

        if self._state.adding:
            super().save(*args, **kwargs)
        else:
            super().save(update_fields=['category_name'], *args, **kwargs)
