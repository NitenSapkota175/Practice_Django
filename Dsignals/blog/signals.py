from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init,pre_delete,post_delete,post_save,pre_save,post_init,pre_migrate,post_migrate
from django.core.signals import request_finished,request_started,got_request_exception
from django.db.backends.signals import connection_created
@receiver(user_logged_in,sender=User)
def login_success(sender,request,user,**kwargs):
    print("---------------------------------------------------------------------------------------")

    print('Logged-In Signal.....Run Intro : ')
    print('sender : ',sender)
    print('request : ' , request)
    print('user : ',user)
    print(f'kwargs : {kwargs}')

# user_logged_in.connect(login_success,sender=User) you can use this a manual connector or decorator like above

@receiver(user_logged_out,sender=User)
def log_out(sender,request,user,**kwargs):
    print("---------------------------------------")

    print('Logged-out Signal.....Run outor : ')
    print('sender : ',sender)
    print('request : ' , request)
    print('user : ',user)
    print(f'kwargs : {kwargs}')


# user_logged_out.connect(log_out,sender=User) you can use this a manual connector or decorator like above


@receiver(user_login_failed)
def login_failed(sender,credentials , request,**kwargs):
    print("---------------------------------------")

    print('Login Failed Signal.....Run outor : ')
    print('sender  : ',sender)
    print('request : ' , request)
    print('credentails : ',credentials)
    print(f'kwargs : {kwargs}')


@receiver(pre_save,sender=User)
def at_beginning_save(sender , instance , **kwargs):
    
    print('pre save Signal.....Run outor : ')
    print('sender : ',sender)
    print('Instance : ' , instance)
    print(f'kwargs : {kwargs}')


@receiver(post_save,sender=User)
def at_ending_save(sender , instance,created , **kwargs):
    
    if created: 
        print('Post save Signal.....Run outor : ')
        print("New record")
        print('sender : ',sender)
        print('Instance : ' , instance)
        print('Created : ' , created)
        print(f'kwargs : {kwargs}')
    else:
        print('Post save Signal.....Run outor : ')
        print("Update")
        print('sender : ',sender)
        print('Instance : ' , instance)
        print('Created : ' , created)
        print(f'kwargs : {kwargs}')


@receiver(pre_delete,sender=User)
def at_beginning_delete(sender , instance , **kwargs):
    
    print('at beginning of delete  : ')
    print('sender : ',sender)
    print('Instance : ' , instance)
    print(f'kwargs : {kwargs}')




@receiver(post_delete,sender=User)
def at_beginning_save(sender , instance , **kwargs):
    
    print('post delete Signal... : ')
    print('sender : ',sender)
    print('Instance : ' , instance)
    print(f'kwargs : {kwargs}')


@receiver(pre_init,sender=User)
def at_beginning_save(sender , *args , **kwargs):
    
    print('pre init Signal.....Run outor : ')
    print('sender : ',sender)
    print('*args : ' , *args)
    print(f'kwargs : {kwargs}')


@receiver(post_init,sender=User)
def at_beginning_save(sender , *args, **kwargs):
    
    print('post save Signal.... : ')
    print('sender : ',sender)
    print('*args : ' , *args)
    print(f'kwargs : {kwargs}')


@receiver(request_started)
def at_beginning_request(sender,environ, **kwargs):
    print('-------------------------------------------------------------')
    print("At the beginning request")
    print('sender', sender)
    print('Environ', environ)
    print('kwrags', kwargs)

@receiver(request_finished)
def at_beginning_request(sender, **kwargs):
    print('-------------------------------------------------------------')
    print("Request Finished : ")
    print('sender', sender)
    print('kwrags', kwargs)

@receiver(got_request_exception)
def at_beginning_request(sender,environ, **kwargs):
    print('-------------------------------------------------------------')
    print("At the request exception..........")
    print('sender', sender)
    print('Environ', environ)
    print('kwrags', kwargs)


@receiver(pre_migrate)
def before_install_app(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
    print('----------------------------------------------------------------------------------')
    print('before_install_app ................')
    print('sender : ',sender)
    print('app config' , app_config)
    print('verbosity : ', verbosity)
    print('Interactive : ',interactive)
    print('using : ',using)
    print('apps',apps)
    print('kwargs' , kwargs)



@receiver(post_migrate)
def at_the_end_of_the_migrate(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
    print('----------------------------------------------------------------------------------')
    print('after_install_app ................')
    print('sender : ',sender)
    print('app config' , app_config)
    print('verbosity : ', verbosity)
    print('Interactive : ',interactive)
    print('using : ',using)
    print('apps',apps)
    print('kwargs' , kwargs)


@receiver(connection_created)
def con_db(sender,connection,**kwargs):
    print('------------------------------------------------------')
    print('coonection databae')
    print('sender' , sender)
    print('connection' , connection)
    print('kwargs',kwargs)
