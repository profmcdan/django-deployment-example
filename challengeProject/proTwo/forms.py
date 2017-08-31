from django import forms
from proTwo.models import User

class NewUserForm(forms.ModelForm):
    # U can do custom validation here
    class Meta: # or Meta()
        model = User
        fields = '__all__'
