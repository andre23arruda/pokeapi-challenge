from django.db import models


class Pokemon(models.Model):
    number = models.SmallIntegerField()
    created_at = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=50)
    types = models.CharField(max_length=50)
    height = models.FloatField()
    weight = models.FloatField()
    sprite = models.CharField(max_length=200)

    def __str__(self):
        return self.name