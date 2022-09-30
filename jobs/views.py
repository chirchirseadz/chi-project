from re import template
from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import PostJobForm, JobProposalForm, TalentRequestForm, HireTalentRequestForm, HireTermsAndConditionForm
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages

# Create your views here.
# page request 
# Request job logics
def jobrequest(request):
    if request.method == 'POST':
        request_form = TalentRequestForm(request.POST)
        if request_form.is_valid():
            request_form.save()
            conditions = request_form.cleaned_data.get("terms_and_conditions")
            first_name = request_form.cleaned_data.get('first_name')
            email = request_form.cleaned_data.get('email')

            if conditions == False:
                messages.error(request, "Kindly Read and check the terms and conditions !!!" )
                return redirect("job_request_form")
            
            else:
                send_user_email_template = render_to_string('emails/email_job_request_notification.html', {'name': first_name})
                job_request_email_template = render_to_string('emails/email_job_request.html', {'name': first_name})

                # This email is sent to the user

                email_message = EmailMessage(
                'Message from Admin chi-squareconnections regarding your Job Request', # here we have the subject
                    send_user_email_template, # here is the body message ):
                    settings.EMAIL_HOST_USER, # This is the sender
                    [email,] # This is the recepient 
                )
                email_message.fail_silently = False
                email_message.send()

                # This is the email sent to notify the admin for the request made from the site

                email_message = EmailMessage(
                'New Jobseeker Alert !! ', # here we have the subject
                    job_request_email_template, # here is the boy message ):
                    email, # This is the sender
                    [settings.EMAIL_HOST_USER,] # This is the recepient 
                )
                email_message.fail_silently = False
                email_message.send()
                request_form.save()
                messages.success(request, "Your Request has been successfully sent !! ")
                return redirect('landing_page')

                  
            
    else:
        request_form = TalentRequestForm()
    context = {
        'request_form': request_form
    }
    return render(request, 'jobs/jobrequest.html', context)

# Sign the Agreement 

def hire_terms_and_conditions(request):
    if request.method == "POST":
        terms_and_conditions = HireTermsAndConditionForm(request.POST)
        if terms_and_conditions.is_valid():
            terms_and_conditions.save(commit)
            condition = terms_and_conditions.cleaned_data.get("terms_and_conditions")
            if condition == True:
                messages.success(request, "You have agreed With Chi-square Connections terms and conditions ")
                return redirect("hire_request_form")

            else :
                messages.error(request, "You have'nt agreed With Chi-square Connections terms and conditions !!")
                return redirect("hire_terms_and_conditions")
            
    
    else:
        terms_and_conditions = HireTermsAndConditionForm()
        condition = terms_and_conditions
    context = {

        "terms_and_conditions":terms_and_conditions,
        "condition":condition
    }
    return render(request, 'jobs/hire_terms_and_conditions.html', context)

# hire talent logics

def hirerequest(request):
    if request.method == 'POST':
        hire_request_form = HireTalentRequestForm(request.POST)
        if  hire_request_form.is_valid():
            hire_request_form.save()
            conditions = hire_request_form.cleaned_data.get("terms_and_conditions")
            first_name =  hire_request_form.cleaned_data.get('first_name')
            email =  hire_request_form.cleaned_data.get('email')

            job_hire_email_template = render_to_string('emails/email_hire_request.html', {'name': first_name})
            hire_admin_send_user_email_template = render_to_string('emails/email_hire_notification.html', {'name': first_name})


            #  Check if user has Agreed with the terms and conditions of the company

            if conditions == False:
                messages.error(request, "Kindly Read and check the terms and conditions !!! ")
                return redirect("hire_request_form")
            else:
                email_message = EmailMessage(
                'Message from Admin chi-squareconnections regarding your Job Request', # here we have the subject
                    hire_admin_send_user_email_template, # here is the boy message ):
                    settings.EMAIL_HOST_USER, # This is the sender
                    [email,] # This is the recepient 
                )
                email_message.fail_silently = False
                email_message.send()

                # This is the email sent to notify the admin for the request made from the site

                email_message = EmailMessage(
                'Job Hire Request Alert !! ', # here we have the subject
                    job_hire_email_template, # here is the boy message ):
                    email, # This is the sender
                    [settings.EMAIL_HOST_USER,] # This is the recepient 
                )
                email_message.fail_silently = False
                email_message.send()
                # This email is sent to the user
                hire_request_form.save()
                messages.success(request, "Your Request has been successfully sent !! ")
                return redirect('landing_page')

                  
            
    else:
        hire_request_form = HireTalentRequestForm()
        condition = hire_request_form
    context = {
        'hire_request_form':  hire_request_form,
      
    }
    return render(request, 'jobs/hiretalent.html', context)


# end


@login_required(login_url='login')
def post_job(request):
    if request.method == 'POST':
        post_job = PostJobForm(request.POST)
        if post_job.is_valid(): 
            post_job.save(commit=False)
            terms_and_conditons = post_job.cleaned_data['terms_and_conditions']
            if  terms_and_conditons == False:
                return redirect('postjobs_terms_errors')
            else:
                post_job.save()
                messages.success(request, 'Has been posted Successfully')
                return redirect('homepage')
    else:
        post_job = PostJobForm()
    context = {
        'post_job': post_job
    }
    return render(request, 'jobs/postjob.html', context)


@login_required(login_url='login')
def postjobs_terms_errors(request):
    return render(request, 'errors/postjob_terms_error.html')

############################################################

@login_required(login_url='login')
def proposal(request):
    if request.method == 'POST':
        proposal = JobProposalForm(request.POST)
        if proposal.is_valid():
            proposal.save(commit=False)
            terms_and_conditions = proposal.cleaned_data['terms_and_conditions']
            if terms_and_conditions == False:
                return redirect('post_job')
            else: 
                proposal.save()
                return redirect('homepage')
     
    else:
        proposal = JobProposalForm()
    context = {
        'proposal': proposal
        }
            
    return render(request,'jobs/proposal.html', context)

@login_required(login_url='login')
def proposal_terms_errors(request):
    return render(request, 'errors/postjob_terms_error.html')


