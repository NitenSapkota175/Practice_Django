from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField()
    #  name = forms.CharField(initial="Somevalue" , help_text="here only 10 charcter can be written")
    email = forms.EmailField()