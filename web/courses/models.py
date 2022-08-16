from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Science(models.Model):
    """Science model.

        Science areas (i.e, math, pyshics).
    """

    name = models.CharField(max_length=35)
    image = models.ImageField(
        upload_to='sciences/images',
        blank=True,
        null=True
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username."""
        return f'{self.name}'


class Course(models.Model):
    """Course model.

        This will have the caracteristics for every course in the site.
    """

    name = models.CharField(max_length=35)
    active = models.BooleanField(default = True)
    logo = models.ImageField(
        upload_to='curses/logos',
        blank=True,
        null=True
    )
    difficulty = models.IntegerField(
        default=1,    
        validators=[
            MaxValueValidator(15),
            MinValueValidator(1)
        ]
    )
    science = models.ForeignKey(to=Science, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username."""
        return f'{self.name}'