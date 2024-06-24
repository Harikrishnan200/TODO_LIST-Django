from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task', 'priority', 'completed']  # Include other fields as necessary

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize field widgets or initial values if needed
        # For example:
        # self.fields['task'].widget.attrs.update({'class': 'form-control'})
