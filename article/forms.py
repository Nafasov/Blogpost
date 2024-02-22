from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'image', 'article', 'massage']
        exec = ['article']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'id': 'name',
            'name': 'name',
            'placeholder': 'Name',
        })
        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'id': 'image',
            'name': 'image',
        })
        self.fields['massage'].widget.attrs.update({
            'class': 'form-control w-10',
            'id': 'comment',
            'name': 'comment',
            'placeholder': "Write Comment",
            'rows': 9,
            'cols': 30,

        })

