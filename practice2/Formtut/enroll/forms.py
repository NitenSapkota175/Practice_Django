from django import forms

class StudentRegistration(forms.Form):
    
        name  = forms.CharField( min_length= 5 , max_length=50,strip=False,
        empty_value="Niten",error_messages={'required' : 'enter your name'}) # if empty value is give the you can submit the empty field no required error 

        agree =  forms.BooleanField(label="I Agree") 
        email = forms.EmailField()

        roll = forms.IntegerField(min_value=5 , max_value=15)

        price = forms.DecimalField(min_value=5 , max_value=15 , max_digits = 4 , decimal_places = 1)

        rate = forms.FloatField(min_value=5 , max_value=15)