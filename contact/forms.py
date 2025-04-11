from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'Placeholder':'Digite seu nome aqui'
            }
        ),
        label='Primeiro Nome',
        help_text='Basta Digitar o seu nome'
    )

    class Meta:
        model = models.Contact
        fields = 'first_name', 'last_name' , 'phone' , 'email' , 'description' , 'category' ,


    def clean(self):
        cleaned_data = self.cleaned_data
        if cleaned_data.get('first_name') == '':
            self.add_error(
                'first_name', ValidationError(
                    'Campo Obrigatório',
                    code = 'invalid'
                )
            )
        
        if cleaned_data.get('last_name')=='':
            self.add_error(
                'last_name',
                ValidationError(
                    'Campo obrigatório!',
                    code = 'invalid'
                )
            )

        return super().clean()



    def clean_firts_name(self):
        first_name = self.cleaned_data.get('first_name')
        return first_name

