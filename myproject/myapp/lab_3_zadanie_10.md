werus@macbook-air-weronika myproject % python3 manage.py shell  
>>> from myapp.models import Osoba
>>> wszystkie_osoby = Osoba.objects.all()
>>> 
>>> print(wszystkie_osoby) 
<QuerySet [<Osoba: Adrian Albrecht>, <Osoba: Maja Binkiewicz>, <Osoba: Roman Cieślak>, <Osoba: Hestia Hamak>, <Osoba: Marta Popielska>]>
>>> osoba_trzy = Osoba.objects.get(id=3)
>>> print(osoba_trzy)
Maja Binkiewicz
>>> Osoba.objects.filter(nazwisko__startswith="B")
<QuerySet [<Osoba: Maja Binkiewicz>]>
>>> unikalne_stanowiska = Osoba.objects.values('stanowisko__nazwa').distinct()
>>> print(unikalne_stanowiska)
<QuerySet [{'stanowisko__nazwa': 'Wykładowca'}, {'stanowisko__nazwa': 'Student'}, {'stanowisko__nazwa': 'Rektor'}, {'stanowisko__nazwa': 'Magister'}, {'stanowisko__nazwa': 'Student'}]>
>>> unikalne_stanowiska = Osoba.objects.values('stanowisko__nazwa').distinct().order_by('stanowisko__nazwa')
>>> print(unikalne_stanowiska)
<QuerySet [{'stanowisko__nazwa': 'Magister'}, {'stanowisko__nazwa': 'Rektor'}, {'stanowisko__nazwa': 'Student'}, {'stanowisko__nazwa': 'Wykładowca'}]>
>>> unikalne_stanowiska = Osoba.objects.values('stanowisko__nazwa').distinct().order_by(-'stanowisko__nazwa')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: bad operand type for unary -: 'str'
>>> unikalne_stanowiska = Osoba.objects.values('stanowisko__nazwa').distinct().order_by('-stanowisko__nazwa')
>>> print(unikalne_stanowiska)
<QuerySet [{'stanowisko__nazwa': 'Wykładowca'}, {'stanowisko__nazwa': 'Student'}, {'stanowisko__nazwa': 'Rektor'}, {'stanowisko__nazwa': 'Magister'}]>
>>> stanowisko = Stanowisko.objects.get(nazwa="Magister")
>>> nowa_osoba = Osoba(imie="Alex", nazwisko="Sałata", plec="M", stanowisko=stanowisko)
>>> nowa_osoba.save()
>>> print(nowa_osoba)
Alex Sałata
>>> exit()




