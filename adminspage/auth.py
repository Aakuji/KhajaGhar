from django.shortcuts import redirect


#to check user 

def unauthenticated_user(view_function):
    def wrapper_function(request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_function(request,*args, **kwargs)
    return wrapper_function

# given access to admin page if request comes from admin
# if request is from normal user redirect to user dashboard

def admin_only(view_function):
        def wrapper_function(request,*args, **kwargs):
            if request.user.is_staff:
                return view_function(request,*args, **kwargs)
            else:
                return redirect('/')
        return wrapper_function

#         #for normal user
# def user_only(view_function):
#     def wrapper_function(request,*args, **kwargs):
#         if request.user.is_staff:
#             return redirect('/')
#         else:
#             return view_function(request,*args, **kwargs)
#     return wrapper_function
