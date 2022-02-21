
from django.shortcuts import render
from contact.form import ContactForm
from django.contrib import messages

from contact.models import Contact

# Create your views here.


def contactnew(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        print(form)
        if form.is_valid:
            try:
                print("valid")
                form.save()
                message = messages.success(request, "successfully send")
            except:
                print("connot send")

    else:
        form = ContactForm()
        print("invalid")
    return render(request, 'mainpage.html', {'form': form, 'message': message})


def contactview(request):
    if(request.method == "POST"):
        page = int(request.POST['page'])
        if('prev' in request.POST):
            page = page-1
        if ('next' in request.POST):
            page = page+1
        tempOffSet = page - 1
        offset = tempOffSet*4
        print(offset)
    else:
        offset = 0
        page = 1
    feedbacks = Contact.objects.raw(
        "select * from contact_contact limit 4 offset % s", [offset])
    pageItem = len(feedbacks)
    return render(request, 'contactview.html', {'feedbacks': feedbacks, 'page': page, 'pageItem': pageItem})
