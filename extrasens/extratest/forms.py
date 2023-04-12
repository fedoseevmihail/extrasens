from django import forms

class UserForm(forms.Form):
    num_user = forms.CharField(max_length=100)
