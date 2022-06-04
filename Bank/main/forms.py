from django import forms


class CreateNewRequest(forms.Form):
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

    name = forms.CharField(label="Name", max_length=25)
    first_surname = forms.CharField(label="First surname", max_length=25)
    second_surname = forms.CharField(label="Second surname", max_length=25)
    cell_number = forms.IntegerField(label="Cell phone number")
    birthday = forms.CharField(label="Birthday", max_length=10)
    birthplace = forms.CharField(label="Birthplace", max_length=25)
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    email = forms.EmailField(label="Email")
    card_type = forms.ChoiceField(choices=CARD_TYPE_CHOICES)
    income = forms.IntegerField(label="Income")
    curp = forms.CharField(label="CURP", max_length=25)
