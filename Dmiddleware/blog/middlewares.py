from django.shortcuts import HttpResponse

# function based middleware
# def my_middleware(get_response):
#     print("One time initialization")

#     def my_function(request):
#         print('This is before view')
#         response = get_response(request)
#         print('this is after view')
#         return response
    
#     return my_function

########### example of one middlleware
# class my_middleware:
#     def __init__(self,get_response):
#         self.get_response = get_response
#         print("One time initialization")


#     def __call__(self,request):
#         print('This is before view')
#         response = self.get_response(request)
#         print('After views')
#         return response


##################### more than one middleware ################################

# class BotherMiddleware:
#     def __init__(self,get_response):
#         self.get_response = get_response
#         print("One time initialization from BotherMiddleware")


#     def __call__(self,request):
#         print('This is BotherMiddleware before view')
#         response = self.get_response(request)
#         print('BotherMiddleware After views')
#         return response


# class FatherMiddleware:
#     def __init__(self,get_response):
#         self.get_response = get_response
#         print("One time initialization from FatherMiddleware")


#     def __call__(self,request):
#         print('This is FatherMiddleware before view')
#         response = self.get_response(request)
#         # response = HttpResponse("return from father")
#         print('FatherMiddleware After views')
#         return response


# class MotherMiddleware:
#     def __init__(self,get_response):
#         self.get_response = get_response
#         print("One time initialization from MotherMiddleware")


#     def __call__(self,request):
#         print('This is MotherMiddleware before view')
#         response = self.get_response(request)
#         print('MotherMiddleware After views')
#         return response


##################################### Hooks ###############################

class MyProcessMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        response = self.get_response(request)
        return response

    def process_view(request,*args,**kwargs):
        print('this is process view before view')
        # return HttpResponse('This is before view') 
        return None ## if none is returned than the control is passed to views
    

########################################### My Exception views #########################################


class MyExceptionMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        response = self.get_response(request)
        return response

    def process_exception(self,request,exception):
        msg = exception
        return HttpResponse(msg)


#########################################template response hook ##################################


class MyTemplateResponseMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        response = self.get_response(request)
        return response

    def process_template_response(self,request,response):
        print('process template respose middleware')
        response.context_data['name'] = 'Sonam'
        return response