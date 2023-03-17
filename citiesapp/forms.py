from django import forms
from django.forms import TextInput, Textarea

from .models import Comment

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('text', )

        #En caso de que se quiera aplicar estilos al form
        widgets = {
            'author': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Author',
                'id': 'formName'
                }),
            'text': Textarea(attrs={
                'class': "form-control", 
                'placeholder': 'Comment',
                'style': 'max-width: 300px;',
                'id': 'formComment'
                })
        }

#Se crea formulario para los Comments
