from django.db import models

# Create your models here.
class Request(models.Model):
    BLACK = 'BL'
    GOLDEN = 'GD'
    SILVER = 'SV'
    CARD_TYPE_CHOICES = [
        (BLACK, 'Black'),
        (GOLDEN, 'Golden'),
        (SILVER, 'Silver'),
    ]

    FEMALE = 'F'
    MALE = 'M'
    GENDER_CHOICES = [
        (FEMALE, 'Female'),
        (MALE, 'Male'),
    ]

    name = models.CharField(max_length=25)
    first_surname = models.CharField(max_length=25)
    second_surname = models.CharField(max_length=25)
    cell_number = models.BigIntegerField()
    birthday = models.CharField(max_length=10)
    birthplace = models.CharField(max_length=25)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default=MALE
    )
    email = models.EmailField()
    card_type = models.CharField(
        max_length=2,
        choices=CARD_TYPE_CHOICES,
        default=SILVER
    )
    income = models.IntegerField()
    curp = models.CharField(max_length=25)


    def __str__(self):
        return self.curp
