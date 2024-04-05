from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {}
    return render(request, 'myApp/home.html', context)

def contract_page(request):
    context = {}
    return render(request, 'myApp/Contract.html', context)

def hobbie_page(request):
    context = {}
    return render(request, 'myApp/Hobbies.html', context)

def send_email(request):
    if request.method == 'POST':
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        sender = request.POST.get('sender', '')
        recipient = ['shaileshsingh00265@gmail.com']  

        send_mail(subject, message, sender, recipient)
        return HttpResponse('Email sent successfully!')
    else:
        return HttpResponse('Invalid request method!')
