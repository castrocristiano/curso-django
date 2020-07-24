from django import forms


class ContactCourse(forms.Form):
   name = forms.CharField(label='Nome', max_length=100)
   email = forms.EmailField(label='E-mail', max_length=100)
   message = forms.CharField(
      label='Mensagem/Dúvida',
      widget=forms.Textarea
   )

