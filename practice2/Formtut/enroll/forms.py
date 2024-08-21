from django import forms

class StudentRegistration(forms.Form):
    
        name = forms.CharField()
        email = forms.EmailField()
        password = forms.CharField(widget=forms.PasswordInput)


        # def clean_name(self):
        #         valname =  self.cleaned_data['name']
        #         if len(valname) < 4:
        #                 raise forms.ValidationError("Enter more that or equal 4 char")
                
        #         return valname




        
        #fields name 

        # name  = forms.CharField( min_length= 5 , max_length=50,strip=False,
        # empty_value="Niten",error_messages={'required' : 'enter your name'}) # if empty value is give the you can submit the empty field no required error 

        # agree =  forms.BooleanField(label="I Agree") 
        

        # roll = forms.IntegerField(min_value=5 , max_value=15)

        # price = forms.DecimalField(min_value=5 , max_value=15 , max_digits = 4 , decimal_places = 1)

        # rate = forms.FloatField(min_value=5 , max_value=15)

        # email = forms.EmailField(min_length=5,max_value=50)

        # website = forms.URLField(min_length=5,max_length=50)

        
        