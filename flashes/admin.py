from django.contrib import admin
from .models import Zpravy, Kolotoc


class ZpravyAdmin(admin.ModelAdmin):
    list_display = ( 'titulek', 'hlavni', 'datum')

class KolotocAdmin(admin.ModelAdmin):
    list_display = ( 'titulek', 'zprava')

admin.site.register(Zpravy, ZpravyAdmin)
admin.site.register(Kolotoc, KolotocAdmin)
