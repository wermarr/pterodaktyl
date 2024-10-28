from django.contrib import admin

# Register your models here.
from .models import Team, Person

admin.site.register(Team)
admin.site.register(Person)

from .models import Osoba, Stanowisko

admin.site.register(Stanowisko)

class OsobaAdmin(admin.ModelAdmin):
    readonly_fields = ['data_dodania']  

admin.site.register(Osoba, OsobaAdmin)


