from django.shortcuts import render
from django.core.cache import cache

# def home(request):
#     mv = cache.get('movie' , 'has_expired')
#     if mv == 'has_expired':
#         cache.set('movie' , 'Extraction',30)
#         mv = cache.get('movie')

#     return render(request,'enroll/home.html',{'fm' : mv})
# # 
# def home(request):
#     mv = cache.get_or_set('fee',4000,30 , version=2) ## if you want set vlaue for the same key then change the version

#     return render(request,'enroll/home.html',{'fm' : mv})



# def home(request):

#     data = {'name' : 'Niten' , 'roll' : 101}
#     cache.set_many(data,30)
#     sv = cache.get_many(data)
#     print(sv)
#     return render(request,'enroll/home.html',{'stu' : sv})

# def home(request):

 
#     cache.delete('roll',version=2)
    
#     return render(request,'enroll/home.html')

# def home(request):
#     cache.set('roll' , 101, 30)
#     rv = cache.get('roll')
#     print(rv)

#     return render(request,'enroll/home.html',)


# def home(request):
   

#     ### only use increament and decrement aftet settings the value
#     rv = cache.decr('roll' , delta=3) # decrement
#     rv = cache.incr('roll' , delta=3) # increament 
#     print(rv)

#     return render(request,'enroll/home.html',)


def home(request):
   
    cache.clear()

    return render(request,'enroll/home.html',)
