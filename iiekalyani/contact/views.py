from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from contact.models import Contact

# Create your views here.
def index(request):
    return HttpResponse("<h3>hDmtP</h3>")

def contact(request):
    # return HttpResponse("Contact is working")
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        msg = request.POST.get('msg')

        contact = Contact(fname=fname,lname=lname,email=email,mobile=mobile,msg=msg)
        contact.save()
    return render(request, 'contact.html')