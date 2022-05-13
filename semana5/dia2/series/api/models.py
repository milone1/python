from django.db import models

# Create your models here.
class Series(models.Model):
    HORROR = 'horror',
    COMEDY = 'comedy',
    ACTION = 'action',
    DRAMA = 'drama'

    CATEGORIES_CHOICES = {
        (HORROR,'HORROR'),
        (COMEDY,'COMEDY'),
        (ACTION,'ACCION'),
        (DRAMA,'DRAMA')
    }

    name = models.CharField(max_length=100)
    release_data = models.DataField()
    rating = models.IntegerField(default=0)
    category = models.CharField(max_length=10,choices=CATEGORIES_CHOICES)
    def __str__(self):
        return self.name