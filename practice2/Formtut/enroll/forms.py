from django import forms
from django.core import validators



class StudentRegistration(forms.Form):
    name = forms.CharField(min_length= 5,max_length=20 ,error_messages={'required' : 'Enter Your Name'})
    email = forms.EmailField(error_messages={'required' : 'Enter Your email'})
    password = forms.CharField(widget=forms.PasswordInput,error_messages={'required' : 'Enter Your password'})
    rpassword = forms.CharField(widget=forms.PasswordInput,error_messages={'required' : 'Re enter you password'})

    def clean(self):

        cleaned_data = super().clean()
        valpass = cleaned_data.get('password')
        valrpass = cleaned_data.get('rpassword')

        if  valpass is None and valpass != valrpass:
            raise  forms.ValidationError("you password doesn't match ")



































#### custom validator #############################33
# def start_with_s(value):
#         if value[0].lower() != 's' : 
#                 raise forms.ValidationError("Name must start with s or S")




# class StudentRegistration(forms.Form):
    
       

       ######### custom validator ####################
        # name = forms.CharField(validators=[start_with_s])
        # email = forms.EmailField() 
       
       
       
       ######################  built in validators ###################333
       
        # name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
        # email = forms.EmailField()
       
       
       
        # password = forms.CharField(widget=forms.PasswordInput)

        # def clean(self):
                
        #         cleaned_data = super().clean()
        #         valname = cleaned_data['name']
        #         valemail = cleaned_data['email']

        #         if len(valname) < 4 :
        #                 raise forms.ValidationError('Name should be more than 4 charcters')
                
        #         if len(valemail) < 15:
        #                 raise forms.ValidationError('Email should be more than 15 charcters')


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

        
        