from django import forms
from .models import Profile
class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'd-flex align-items-start py-3 border-bottom'}))
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class': 'bg-light form-control'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'bg-light form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'bg-light form-control'}))
    class Meta:
        model = Profile
        fields = ('avatar','firstname', 'lastname', 'email', 'country', 'language')
