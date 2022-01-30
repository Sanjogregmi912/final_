from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from authenticate import Authentication

from user.form import UserForm
@login_required(login_url='/login')
def user_view(request):
    if(request.method == 'POST'):
        page = int(request.POST['page'])
        if('prev' in request.POST):
            page= page-1
        if('next' in request.POST):
            page=page+1
        tempOFFSet = page-1
        offset = tempOFFSet*4
        print(offset)
    else:
        offset=0
        page=1
    users=User.objects.raw("select * from auth_user limit 4 offset %s",[offset])
    pageItem=len(users)
    return render (request,"user/view.html",{'users':users,'page':page,'pageItem':pageItem})
@login_required(login_url='/login')
def user_create(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST["email"]
        password = request.POST["password"]
        user = User.objects.create_user(username=username,email=email,password=password)
        user.save()
        return redirect('/user_view')

    return render(request,'user/create.html')
@login_required(login_url='/login')
def user_edit(request,p_id):
    try:
        user=User.objects.get(id=p_id)
        return render(request,"user/edit.html",{'user':user})
    except:
        print("No data found")
    return redirect('/user_view')
@login_required(login_url='/login')
def user_update(request,p_id):
    user=User.objects.get(id=p_id)
    form=UserForm(request.POST,instance=user)
    if form.is_valid():
        try:
            form.save()
            return redirect("/user_view")
        except:
            print("Cannot update")
    return render(request,"user/edit.html",{'user':user})
@login_required(login_url='/login')
def user_delete(request,p_id):
    try:
        user=User.objects.get(id=p_id)
        user.delete()
    except:
        print("No data found")
    return redirect('/user_view')