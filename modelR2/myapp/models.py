from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True) # user willbe delete but the post is set to null
    post_title = models.CharField(max_length=70)
    post_cat = models.CharField(max_length=70)
    post_publish_date = models.DateField()


