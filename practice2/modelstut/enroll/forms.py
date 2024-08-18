from django import forms

class StudentRegistration(forms.Form):
    
    
    name = forms.CharField()
    email = forms.EmailField()
    mobile = forms.IntegerField()
    key = forms.CharField(widget=forms.HiddenInput()) #hidden feild
    
    
    
    
    # previous tutorial 
    
    # name = forms.CharField()
    # #  name = forms.CharField(initial="Somevalue" , help_text="here only 10 charcter can be written")
    # email = forms.EmailField()