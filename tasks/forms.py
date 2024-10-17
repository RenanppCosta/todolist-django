from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task 
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Insira sua tarefa aqui',
                'class': 'p-2 text-white focus:outline-none bg-gray-400 placeholder-white w-[60%]' 
            })
        }
        