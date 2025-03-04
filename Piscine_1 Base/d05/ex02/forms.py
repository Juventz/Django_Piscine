from django import forms

class LogForm(forms.Form):
    text = forms.CharField(label='Enter text', max_length=200, required=True)