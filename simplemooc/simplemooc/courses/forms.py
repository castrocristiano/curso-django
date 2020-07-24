from django import forms


class ContactCourse(forms.Form):
    name = forms.CharField(
       label='Nome',
       max_length=100
    )
    email = forms.EmailField(
       label='E-mail',
       max_length=100
    )
    age = forms.IntegerField(
        label='Idade',
        min_value=0,
        required=False
    )
    message = forms.CharField(
        label='Mensagem/Dúvida',
        widget=forms.Textarea
    )
