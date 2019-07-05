from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import ContactForm

def successView(request):
    return render(request,'contact-success.html', {})

def contactView(request):
    # contact view, uses the contact form in forms.py
    # response viewable in server log

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email,['photova@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return HttpResponseRedirect('success')
    return render(request,"contact.html",{'form':form})
