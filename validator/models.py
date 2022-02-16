from django.db import models

# Create your models here.

from django.db import models


class Result(models.Model):

    name = models.CharField(max_length=200)
    is_valid_number = models.IntegerField()
    is_valid_result = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name} / {self.is_valid_result}'



