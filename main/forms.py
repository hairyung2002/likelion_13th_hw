from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': '할 일을 입력하세요'})
        }