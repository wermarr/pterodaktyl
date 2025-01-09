from django.db import models
from django.core.validators import RegexValidator



# Create your models here.

# deklaracja statycznej listy wyboru do wykorzystania w klasie modelu
MONTHS = models.IntegerChoices('Miesiace', 'Styczeń Luty Marzec Kwiecień Maj Czerwiec Lipiec Sierpień Wrzesień Październik Listopad Grudzień')

SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )


class Team(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name}"


class Person(models.Model):

    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, default=SHIRT_SIZES[0][0])
    month_added = models.IntegerField(choices=MONTHS.choices, default=MONTHS.choices[0][0])
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)
    pseudonim = models.CharField(max_length=50, default="-")

    def __str__(self):

        return self.name

class Dog(models.Model):
    dog_name = models.CharField(max_length=30)
    dog_breed = models.CharField(max_length=30)

WYBOR_PLEC = (
('K', 'kobieta'),
('M', 'mezczyzna'),
('I', 'inne'),
)

class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=50, null=False, blank=False)
    opis = models.TextField(blank=True)

    def __str__(self):
        return self.nazwa

class Osoba(models.Model):
    imie = models.CharField(max_length=50, null=False, blank=False)
    nazwisko = models.CharField(max_length=50, null=False, blank=False)
    plec = models.CharField(max_length=1, choices=WYBOR_PLEC, blank=False)
    stanowisko = models.ForeignKey(Stanowisko, on_delete=models.CASCADE)
    data_dodania = models.DateField(auto_now_add=True)

    class Meta: 
        ordering = ['nazwisko']

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"


class Zamieszkanie(models.Model): 
    miasto = models.CharField(max_length=60, null=False, blank=False)
    ulica = models.CharField(max_length=60, null=False, blank=False)
    numer_domu = models.IntegerField(null=False, blank=False)
    numer_mieszkania = models.IntegerField(null=True, blank=True)
    kod_pocztowy = models.CharField(
        max_length=6,
        null=False,
        blank=False,
        validators=[RegexValidator(
            regex=r'^\d{2}-\d{3}$',
            message='podaj kod pocztowy w formacie xx-xxx, np. 02-987.',
            code='invalid_postal_code'
        )]
    )

    def __str__(self):
        return f"{self.ulica} {self.numer_domu} {self.miasto}"


    
class Zwierze(models.Model):
    class wybor_zwierze(models.IntegerChoices):
        PIES = 1
        KOT = 2
        KANAREK = 3
        CHOMIK = 4

    suit = models.IntegerField(choices=wybor_zwierze.choices)

def __str__(self):
        return self.wybor_zwierze(self.suit).label

