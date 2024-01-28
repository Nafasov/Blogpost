from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'image', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': "form-control",
            'name': 'name',
            'id': 'name',
            'placeholder': 'Entir your name'

        })
        self.fields['email'].widget.attrs.update({
            'class': "form-control",
            'name': 'email',
            'id': 'email',
            'placeholder': 'Enter email address'

        })
        self.fields['message'].widget.attrs.update({
            'class': "form-control w-100",
            'name': 'message',
            'id': 'message',
            'cols': 30,
            'rows': 9,
            'placeholder': 'Enter message'

        })
        self.fields['image'].widget.attrs.update({
            'class': "form-control",
            'name': 'image',
            'id': 'image',
            'placeholder': 'Enter your image'

        })

