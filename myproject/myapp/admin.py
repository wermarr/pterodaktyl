from django.contrib import admin

# Register your models here.
from .models import Team, Person

admin.site.register(Team)
admin.site.register(Person)

from .models import Osoba, Stanowisko, Zamieszkanie

admin.site.register(Stanowisko)

class OsobaAdmin(admin.ModelAdmin):
    readonly_fields = ['data_dodania']  
    list_display = ["nazwisko", "imie", "stanowisko_z_id", "data_dodania"]
    
    @admin.display(description='Stanowisko (id)')
    def stanowisko_z_id(self, obj):
        return f"{obj.stanowisko} ({obj.stanowisko.id})"


admin.site.register(Osoba, OsobaAdmin)

admin.site.register(Zamieszkanie)

from .models import Zwierze

admin.site.register(Zwierze)


