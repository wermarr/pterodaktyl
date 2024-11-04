from django.contrib import admin

# Register your models here.
from .models import Team, Person

admin.site.register(Team)
admin.site.register(Person)

from .models import Osoba, Stanowisko, Zamieszkanie

class StanowiskoAdmin(admin.ModelAdmin):
    list_display = ('nazwa', 'opis') 
    search_fields = ('nazwa',)  

admin.site.register(Stanowisko, StanowiskoAdmin)

class OsobaAdmin(admin.ModelAdmin):
    readonly_fields = ['data_dodania']  
    list_display = ["nazwisko", "imie", "stanowisko_z_id", "data_dodania"]
    list_filter = ('stanowisko', 'data_dodania')  
    
    @admin.display(description='Stanowisko (id)')
    def stanowisko_z_id(self, obj):
        return f"{obj.stanowisko} ({obj.stanowisko.id})"


admin.site.register(Osoba, OsobaAdmin)

admin.site.register(Zamieszkanie)

from .models import Zwierze

admin.site.register(Zwierze)


