from django import forms
from .models import Event

#


class form_class(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["memo"]
