from django import forms
from .models import ToDo

class ToDoForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "What's on your mind...",
        "size":"50",
    }))
    class Meta:
        model = ToDo
        fields = [
            'name',
        ]