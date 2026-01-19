from django import forms
from .models import EntradaProducao

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class EntradaProducaoForm(forms.ModelForm):
    class Meta:
        model = EntradaProducao

        fields = '__all__'

        exclude = ['tempoParado', 'tempoProduzido']