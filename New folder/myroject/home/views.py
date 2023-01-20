from django.shortcuts import render,HttpResponse
from home.models import Contact
# Create your views here.

def index(request):
    return render(request,"index.html")
    

def contact(request):
    if request.method == "POST":
        name = request.POST.get("mane")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        message = request.POST.get("message")
        contact = Contact(name=name,email=email,phone=phone, password= password , message=message)
        contact.save()
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")
    
def blog(request):
    return render(request, "blog.html")
