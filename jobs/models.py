from django.db import models
from users.models import user_profile, AreaOfSpecialization
# Create your models here.

class JobPost(models.Model):

    employer = models.OneToOneField(user_profile, on_delete=models.CASCADE, null =True)
    area_of_specialization = models.ForeignKey(AreaOfSpecialization, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100,null=True)
    job_desc =  models.TextField(blank=True)
    budget =  models.FloatField()
    date_posted = models.DateTimeField(auto_now_add=True)
    terms_and_conditions = models.BooleanField(default=False)
    job_taken = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.title}'
    
class jobrequest(models.Model):
    TERMS_OF_SERVICE = (
        ('Contract','Contract'),
        ('Temporary','Temporary'),
        ('Permanent','Permanent'),
        

    )
    user_requesting = models.OneToOneField(user_profile, on_delete=models.CASCADE, null=True)
    area_of_specialization = models.ForeignKey(AreaOfSpecialization, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100,null=True)
    proposal = models.TextField(blank=True)
    terms_of_service = models.CharField(max_length=100, choices=TERMS_OF_SERVICE, null=True)
    your_budget = models.FloatField()
    terms_and_conditions = models.BooleanField(default=False)
    
       
        
    def __str__(self):
            return f'{self.title}'

class TalentRequest(models.Model):
  
    LOCATION = (
         ('Nairobi City','Nairobi City'),
            ('Mombasa', 'Mombasa'),
            ('Kwale', 'Kwale'),
            ('Kilifi', 'Kilifi'),
            ('Tana River', 'Tana River'),
            ('Lamu','Lamu'),
            ('Taita-Taveta','Taita-Taveta'),
            ('Garissa','Garissa'),
            ('wajir','wajir'),
            ('Mandera','Mandera'),
            ('Marsabit', 'Marsabit'),
            ('Isiolo','Isiolo'),
            ('Meru','Meru'),
            ('Tharaka-Nithi','Tharaka-Nithi'),
            ('Embu','Embu'),
            ('Kitui','Kitui'),
            ('Machakos','Machakos'),
            ('Makueni','Makueni'),
            ('Nyandarua','Nyandarua'),
            ('Nyeri','Nyeri'),
            ('Kirinyaga','Kirinyaga'),
            ("Murang'a", "Murang'a"),
            ('Kiambu','Kiambu'),
            ('Turkana','Turkana'),
            ('West Pokot','West Pokot'),
            ('Samburu','Samburu'),
            ('Trans Nzoia','Trans Nzoia'),
            ('Uasin Gishu','Uasin Gishu'),
            ('Elgeyo-Marakwet','Elgeyo-Marakwet'),
            ('Nandi','Nandi'),
            ('Baringo','Baringo'),
            ('Laikipia','Laikipia'),
            ('Nakuru','Nakuru'),
            ('Narok','Narok'),
            ('Kajiado','Kajiado'),
            ('Kericho','Kericho'),
            ('Bomet','Bomet'),
            ('Kakamega','Kakamega'),
            ('Vihiga','Vihiga'),
            ('Bungoma','Bungoma'),
            ('Busia','Busia'),
            ('Siaya','Siaya'),
            ('Kisumu','Kisumu'),
            ('Homa Bay','Homa Bay'),
            ('Migori','Migori'),
            ('Kisii','Migori'),
            ('Nyamira','Nyamira'),
            
    )
    SERVICE = (
        ('Contract','Contract'),
        ('Temporary','Temporary'),
        ('Parmanent','Parmanent'),
    )
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True, unique=True)
    area_of_specialization = models.ForeignKey(AreaOfSpecialization, on_delete=models.CASCADE,null=True)
    job_title = models.CharField(max_length=100, null =True)
    your_info = models.TextField(blank=True)
    location = models.CharField(max_length=100, choices=LOCATION, null=True)
    phone_number = models.CharField(max_length=100, null=True)
    terms_of_service =  models.CharField(max_length=100, choices=SERVICE, null=True)
    date_of_request = models.DateTimeField(auto_now=True)
    terms_and_conditions = models.BooleanField(default=False)

    def __str__(self):
        return self.job_title


class HireTalentRequest(models.Model):
    
    LOCATION = (
            ('Nairobi City','Nairobi City'),
            ('Mombasa', 'Mombasa'),
            ('Kwale', 'Kwale'),
            ('Kilifi', 'Kilifi'),
            ('Tana River', 'Tana River'),
            ('Lamu','Lamu'),
            ('Taita-Taveta','Taita-Taveta'),
            ('Garissa','Garissa'),
            ('wajir','wajir'),
            ('Mandera','Mandera'),
            ('Marsabit', 'Marsabit'),
            ('Isiolo','Isiolo'),
            ('Meru','Meru'),
            ('Tharaka-Nithi','Tharaka-Nithi'),
            ('Embu','Embu'),
            ('Kitui','Kitui'),
            ('Machakos','Machakos'),
            ('Makueni','Makueni'),
            ('Nyandarua','Nyandarua'),
            ('Nyeri','Nyeri'),
            ('Kirinyaga','Kirinyaga'),
            ("Murang'a", "Murang'a"),
            ('Kiambu','Kiambu'),
            ('Turkana','Turkana'),
            ('West Pokot','West Pokot'),
            ('Samburu','Samburu'),
            ('Trans Nzoia','Trans Nzoia'),
            ('Uasin Gishu','Uasin Gishu'),
            ('Elgeyo-Marakwet','Elgeyo-Marakwet'),
            ('Nandi','Nandi'),
            ('Baringo','Baringo'),
            ('Laikipia','Laikipia'),
            ('Nakuru','Nakuru'),
            ('Narok','Narok'),
            ('Kajiado','Kajiado'),
            ('Kericho','Kericho'),
            ('Bomet','Bomet'),
            ('Kakamega','Kakamega'),
            ('Vihiga','Vihiga'),
            ('Bungoma','Bungoma'),
            ('Busia','Busia'),
            ('Siaya','Siaya'),
            ('Kisumu','Kisumu'),
            ('Homa Bay','Homa Bay'),
            ('Migori','Migori'),
            ('Kisii','Migori'),
            ('Nyamira','Nyamira'),
            

        
    )
    SERVICE = (
        ('Contract','Contract'),
        ('Temporary','Temporary'),
        ('Parmanent','Parmanent'),
    )
   
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True, unique=True)
    area_of_need = models.ForeignKey(AreaOfSpecialization, on_delete=models.CASCADE,null=True)
    job_title = models.CharField(max_length=100, null =True)
    your_specifications = models.TextField(blank=True)
    phone_number = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, choices=LOCATION, null=True)
    terms_of_service =  models.CharField(max_length=100, choices=SERVICE, null=True)
    date_of_request = models.DateTimeField(auto_now=True)
    terms_and_conditions = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.job_title





# skills_experience
# job_experience
# budget
# date_posted

