from myapp.models import Osoba, Stanowisko
from myapp.serializers import OsobaSerializer, StanowiskoSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# tworzymy nowe obiekty 

stanowisko = Stanowisko.objects.create(nazwa = "kierownik", opis = "zarządza tymi co zarządzają")
osoba = Osoba.objects.create(imie = "Jan", nazwisko = "Malinowski", plec = 2, stanowisko = stanowisko)

# inicjalizacja serializera dla Osoba 

osoba_serializer = OsobaSerializer(osoba)
print(osoba_serializer.data)

# wynik powinien byc {'id': 6, 'imie' : 'Jan', 'nazwisko' : 'Malinowski', 'plec': 'Męzczyzna', 'stanowisko' : 4, 'data_dodania':'2025-01-09'}

osoba_json = JSONRenderer().render(osoba_serializer.data)

import io 

# strumien danych JSON 

stream = io.BytesIO(osoba_json)

# pasowanie JSON do slownika 

data = JSONParser().parse(stream)

# tworzymy obiekt deserializera dla danych JSON 

deserializer = OsobaSerializer(data = data)

# walidacja danych 
print(deserializer.is_valid)
print(deserializer.errors)

# bledne dane 
invalid_data = {'imie': 'Adam', 'nazwisko': 'Nowak', 'plec' : 'Nieznany', 'stanowisko': stanowisko.id }

# serializer z blednymi danymi 
invalid_serializer = OsobaSerializer(data= invalid_data)

print(invalid_serializer.is_valid())
print(invalid_serializer.errors)

if deserializer.is_valid():
    deserializer.save()
    

# inicjowanie serializera dla stanowiska 

stanowisko_serializer = StanowiskoSerializer(stanowisko)
print(stanowisko_serializer.data)

# serilaizacja do JSON 

stanowisko_json = JSONRenderer().render(stanowisko_serializer.data)
print(stanowisko_json)

# {'id' : 1, 'nazwa' : 'kierownik', 'opis':'zarzadza tymi co zarzadzaja'}

# deserializacja z JSON 
stream = io.Bytes(stanowisko_json)
data = JSONParser().parse(stream)

desrializer = StoniwskoSerializer(data = data)

print( deserializer.is_valid())

if deserializer.is_valid():
    deserializer.save()



