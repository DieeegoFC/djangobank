from django.db import models

# Create your models here.
class Request(models.Model):
    name = models.CharField(max_length=25)
    first_surname = models.CharField(max_length=25)
    second_surname = models.CharField(max_length=25)
    cell_number = models.BigIntegerField()
    birthday = models.CharField(max_length=10)
    birthplace = models.CharField(max_length=25)
    sex = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    card_type = models.CharField(max_length=25)
    income = models.IntegerField()
    curp = models.CharField(max_length=25)

    def __str__(self):
        return self.curp
