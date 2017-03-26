from django import forms
from .models import Zpravy


class ZpravyForm(forms.ModelForm):

    class Meta:
        model = Zpravy
        fields = [ 'titulek', 'obsah', 'obrazek' ]
