from django.shortcuts import render
from django.core.mail import send_mail



send_mail(
    'Testing Mail',
    'Here is the message.',
    'tanayadodal444@gmail.com',
    ['tanayadodal444@gmail.com'],
    fail_silently=False,
)

def learn(request):
    return render(request,'one.html')
