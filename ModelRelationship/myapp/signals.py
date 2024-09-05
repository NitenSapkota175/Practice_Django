from . models import Page
from django.db.models.signals import post_delete
from django.dispatch import receiver

### this is whenever you delete page user will also get deleted
@receiver(post_delete,sender=Page)
def delete_related_user(sender,instance,**kwargs):
    
    print("Page post delete")
    instance.user.delete()
