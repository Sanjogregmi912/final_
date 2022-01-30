from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect
class Authentication:
    def valid_user(function):
        def wrap(request):
            print(request)
            try:
                User.objects.get(email=request.session['email'],password=request.session['password'])
                return function(request)
            except:
                print('no authentication')
                messages.warning(request,'NOTE  : Please login first to get access')
                return redirect('/login')
        return wrap
    def valid_user_where_id(function):
        def wrap(request,p_id):
            try:
                User.objects.get(email=request.session['email'],password=request.session['password'])
                return function(request,p_id)
            except:
                messages.warning(request,'Please enter a valid username and password')
                return redirect('/login')
        return wrap