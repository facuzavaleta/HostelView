from django import forms
from django.forms.widgets import TextInput, Textarea, NumberInput
from .models import Accommodation

class AccommodationForm(forms.ModelForm):
    name = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=Textarea(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}))
    country = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}))
    # photo = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))
    rooms_number = forms.IntegerField(widget=NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Accommodation
        fields = ['name', 'description', 'address', 'city', 'country', 'rooms_number']