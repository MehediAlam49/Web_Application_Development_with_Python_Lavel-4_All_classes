from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def send_email(request):
    user_email = 'mehedialam806@gmail.com'

    send_mail(
        "Practice email",
        "just check mail.",
        "shakil.eub.cse@gmail.com",
        [user_email],
        
    )

    return render(request, 'send_email.html')