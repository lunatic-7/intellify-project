from django.http import HttpResponse
from django.shortcuts import redirect

# To return back logged in user back to home, if he tries to access log in or regiter page while logged in.
# (Wasif)
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("school_home")
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func

# Adding different user to their respective group, so that they can access some pages and some not, according
# to their group
# (Wasif)
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not authorized to view this page!")
        return wrapper_func
    return decorator

# Making some templated to be seen by admin only (Wasif)
def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'customer':
            return redirect('user-page')
        
        if group == 'admin':
            return view_func(request, *args, **kwargs)
    return wrapper_function