from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage

from contact.form import ContactForm

def new(request):
    form = ContactForm

    return render(request, 'form.html', { 'form': form })

def create(request):
    form = ContactForm(request.POST)

    if form.is_valid():
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        sender = form.cleaned_data['sender']

        email = EmailMessage(subject, message, sender, ['adammikulas@gmail.com'])
        email.send()

        return HttpResponseRedirect('/contact/thanks')
    else:
        render(request, 'form.html', { 'form': form })

def thanks(request):
    return render(request, 'thanks.html')
