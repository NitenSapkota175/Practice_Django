from django.db import models
from django.contrib.auth.models import User

class Page(models.Model):
    # user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    # user = models.OneToOneField(User,on_delete=models.PROTECT,primary_key=True) # user object cannot be delted due to protected
    user = models.OneToOneField(User,on_delete=models.PROTECT,primary_key=True,limit_choices_to={'is_staff' : True}) # only staff and admin can create page
    page_name = models.CharField(max_length=70)
    page_cat = models.CharField(max_length=70)
    page_publish_date = models.DateField(max_length=70)




