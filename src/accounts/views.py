from django.db import IntegrityError
from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponseRedirect
from django.contrib import messages
from django.views.decorators.http import require_GET,require_POST
from .forms import Register_form,Login_form
from .models import user
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from accounts.auth_backend import EmailBackend
# Create your views here.

def account_register(request):
    messages.add_message(request=request,level=messages.SUCCESS,message="Profile created sucessfully")
    return render(request=request,template_name='account/register.html',context={})


def register_process(request):
    form = Register_form(request.POST)
    if form.is_valid():
        register = user()
        register.username = request.POST.get('name')
        register.acc_email = request.POST.get('email')
        register.password = register.set_password(raw_password=request.POST.get('password'))
        try:
            register.save()
        except IntegrityError as e: 
            if 'username' in str(e).split('.')[-1]:
                error_field = 'name'
                error = 'User already exists'
            elif 'acc_email' in str(e).split('.')[-1]:
                error_field = 'email'
                error = 'Email already exists'
            return JsonResponse({
                'status':"false",
                'errors':
                    {
                        error_field:error
                    },                
                'validated':"flase"
            })            
        return JsonResponse({
    'status':"true",
    'errors':[],
    'message':"Registered successfully"
})
    else:
        return JsonResponse({
            'status':"false",
            'errors':form.errors,
            'validated':"false"
        })


def account_login(request):
    if request.method == 'POST':
        form = Login_form(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = EmailBackend.authenticate(request,email,password)
            if user is not None:
                login(request,user)
                return redirect('account_profile')
        else:
            return render(request,"account/login.html",{'form':form})

    return render(request,'account/login.html',{})

def account_myAccount(request):
    return render(request=request,template_name='jobs/my_jobs.html',context={})

@login_required
def account_profile(request):
    request.session['login'] = 'My Account'
    return render(request,template_name='account/profile.html',context={})

def account_logout(request):
    logout(request)
    return redirect('index')
"""
requets parameters
['COOKIES', 'FILES', 'GET', 'META', 'POST', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', '_current_scheme_host', '_encoding', '_get_full_path', '_get_post', '_get_raw_host', '_get_scheme', '_initialize_handlers', '_load_post_and_files', '_mark_post_parse_error', '_messages', '_read_started', '_set_content_type_params', '_set_post', '_stream', '_upload_handlers', 'accepted_types', 'accepts', 'auser', 'body', 'build_absolute_uri', 'close', 'content_params', 'content_type', 'csrf_processing_done', 'encoding', 'environ', 'get_full_path', 'get_full_path_info', 'get_host', 'get_port', 'get_signed_cookie', 'headers', 'is_secure', 'method', 'parse_file_upload', 'path', 'path_info', 'read', 'readline', 'readlines', 'resolver_match', 'scheme', 'session', 'upload_handlers', 'user']
"""