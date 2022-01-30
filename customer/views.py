from multiprocessing import AuthenticationError
import re
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from customer.form import CustomerForm
from customer.models import Customer
from authenticate import Authentication
from django.contrib.auth.decorators import login_required






def homepage(request):
    return render(request, 'mainpage.html')


def login(request):
    if request.method == 'POST':
        un = request.POST['username']
        pw = request.POST['password']
        user = auth.authenticate(username=un, password=pw)
        if user is not None:
            auth.login(request, user)
            return redirect('/dashboard')
        else:
            messages.error(request, "bad credentials")
            return redirect('/login')
    return render(request, 'login.html')


def registration(request):
    if(request.method=="POST"):
        form=CustomerForm(request.POST)

        result = form.save()
        print(result.id)
        request.session['customer_id'] = result.id
        return redirect('/games/games_all')
    else:
        form = CustomerForm()
        return render(request,'games/register.html',{'form':form})

@login_required(login_url='/login')
def dashboard(request):
    return render(request,"dashboard.html")
@login_required(login_url='/login')
def view(request):
    if request.method=="POST":
        page =int(request.POST['page'])
        if('prev' in request.POST):
            page=page-1
        if('next' in request.POST):
            page=page+1
        tempOffSet=page - 1
        offset=tempOffSet*4
        print(offset)
    else:
        offset=0
        page=1
        
    customers =Customer.objects.raw("select * from customer_customer limit 4 offset % s",[offset])
    pageItem = len(customers)    
    return render(request,"customers/view.html",{'page':page,'customers':customers,'pageItem':pageItem})
@login_required(login_url='/login')
def customer_create(request):
    if request.method=="POST":
        form=CustomerForm(request.POST)
        print(form)
        if form.is_valid():
            try:
                print("valid")
                form.save()
                return redirect("/view")
            except:
                print("validation failed")
    else:
        form=CustomerForm()
        print("invalid")
    return render(request,"customers/create.html",{'form' :form})

@login_required(login_url='/login')
def customer_edit(request,p_id):
    try:
        customer = Customer.objects.get(id=p_id)
        return render(request,"customers/edit.html",{"customer":customer})
    except:
        print("No data Found")    
        return redirect("/view")

@login_required(login_url='/login')
def customer_update(request,p_id):
    customer = Customer.objects.get(id=p_id)
    form = CustomerForm(request.POST,instance=customer)
    if form.is_valid():
        try:
            form.save()
            return redirect("/view")
        except:
            print("cannot change")
    return render(request,"customers/edit.html",{'customer':customer})
@login_required(login_url='/login')
def customer_delete(request,p_id):
    try:
        customer=Customer.objects.get(id=p_id)
        customer.delete()
    except:
        print("No data Found")
    return redirect("/view")