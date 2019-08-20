from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import ContactForm

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

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

            message = Mail(
                from_email = form.cleaned_data['from_email'],
                to_emails = 'hannahchebetphoto@gmail.com',
                subject = 'CONTACT FORM: ' + form.cleaned_data['subject'],
                html_content = form.cleaned_data['message'],
            )

            try:
                sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
                response = sg.send(message)
                print(response.status_code)
                print(response.body)
                print(response.headers)
                # send_mail(subject, message, from_email,['hannahchebetphoto@gmail.com'])
            except BadHeaderError or Exception as e:
                print(e.message)
                return HttpResponse('Invalid header found')
            return HttpResponseRedirect('success')
    return render(request,"contact.html",{'form':form})
