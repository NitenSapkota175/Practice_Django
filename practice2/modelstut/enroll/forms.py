from django import forms

class StudentRegistration(forms.Form):
    


    password = forms.CharField(widget=forms.PasswordInput)
    key = forms.CharField(widget=forms.HiddenInput)
    comment = forms.CharField(widget=forms.Textarea(attrs={'class' : 'textcss'})) #attrs is used to add attributes to fields like class and id 
    check = forms.CharField(widget=forms.CheckboxInput)
    file = forms.CharField(widget=forms.FileInput)

    # name = forms.CharField(label="Enter your name ",label_suffix=' '
    # ,initial="Niten",required=False,disabled=True,help_text="Limit 70 char")



    
    # name = forms.CharField()
    # email = forms.EmailField()
    # mobile = forms.IntegerField()
    # key = forms.CharField(widget=forms.HiddenInput()) #hidden feild
    
    
    
    
    # previous tutorial 
    
    # name = forms.CharField()
    # #  name = forms.CharField(initial="Somevalue" , help_text="here only 10 charcter can be written")
    # email = forms.EmailField()