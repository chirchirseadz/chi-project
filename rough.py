    # first_name = request.POST['first_name']
        # email = request.POST['email']
        # job_title = request.POST['job_title']
        # your_info = request.POST['your_info']
        
        if request_form.is_valid():
            request_form.save()
            return redirect('homepage')
        #     send_mail(
        #         job_title, #subject
        #         your_info, # message
        #         email, # from email
           
        #     # 'cherokaren@gmailcom'
        #     ['sydneychirchir@gmail.com'], # to email
          
 
        # ),
            
            
        
      
    else:
        request_form = FindTalentRequestForm()
        
    context = {
        'request_form': request_form,
          
    }