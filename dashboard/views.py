from cmath import log
import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from users.models import user_profile
from jobs.forms import TalentRequestForm
from jobs.models import JobPost
from django.contrib.auth.models import User
from jobs.models import TalentRequest
from users.models import AreaOfSpecialization

from .forms import MessageForm
from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail 



# Create your views here.

    

def landing_page(request):
    categories = AreaOfSpecialization.objects.all()
    data = TalentRequest.objects.all()
    context = {
        'data':data,
        'categories': categories
    }
    
    return render(request, 'dashboard/landing_page.html', context)



# @login_required(login_url='login')
def index(request):
    return render(request, 'dashboard/index.html')

def about(request):
    categories = AreaOfSpecialization.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'dashboard/about.html', context)


def blog(request):
    return render(request, 'dashboard/blog.html')



def contact(request):
    if request.method == 'POST':
        # message_sent = False
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            your_name = message_form.cleaned_data.get('your_name')
            email = message_form.cleaned_data.get('email')
            subject = message_form.cleaned_data.get('subject')
            message = message_form.cleaned_data.get('message')
            message_form.save()

            send_mail(


                subject,  # subject 
                message,  # message   
                email, # from 
                ['info@chi-squareconnections.com'], # To email 
                # "This is the message from  chisquare-connections  contact us page ", 
                fail_silently = False
                
                 
            )

            # message_sent = True

            messages.success(request, 'Your message was sent successfully !')

            return redirect('contact')
        

            # return HttpResponse('<script> window.alert("Thanks for your comment")</script>')
    else:
        message_form = MessageForm()
        your_name = MessageForm()
    context = {
        'message_form': message_form,
        'your_name':your_name
    }
    return render(request, 'dashboard/contact.html', context)



def news_and_notices(request):

    return render(request, 'dashboard/news_and_notices.html')


def testimonials(request):
    return render(request, 'dashboard/testimonials.html')





    
################### talent works ###########

# def admin_assistant(request):
#     users = User.objects.all()
#     context = {
#         'users' : users
#     }
#     return render(request, 'dashboard/admin_assistant.html',context)

# def clerk_data_entry(request):
#     return render(request, 'dashboard/clerk_data_entry.html')


# def it_spacialist(request):
#     return render(request, 'dashboard/it_spacialist.html')

# def hospitality(request):
#     return render(request, 'dashboard/hospitality.html')


# def customer_care(request):
#     return render(request, 'dashboard/customer_care.html')

# def hospitality_wait_staff(request):
#     return render(request, 'dashboard/hospitality_wait_staff.html')

