from django.urls import path
from jobs import views

urlpatterns = [
  path('job/request/',views.jobrequest, name='job_request_form'),
  path('hire/request/',views.hirerequest, name='hire_request_form'),
  path('post/job/', views.post_job, name='post_job')  ,
  path('job/proposal/', views.proposal, name='job_proposal'),
  path('postjob/terms_error/', views.postjobs_terms_errors, name='postjobs_terms_errors'),
  path('proposal/terms_error/', views.proposal_terms_errors, name='proposal_terms_errors'),
  
  
  #  Terms and conditions paths 
  
  # path('hire_terms_and_conditions/', views.hire_terms_and_conditions, name='hire_terms_and_conditions'),
  

]
