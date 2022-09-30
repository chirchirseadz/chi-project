from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class AreaOfSpecialization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    more_info = models.TextField(blank=True)
    image  = models.ImageField(default='empty.jpg', upload_to='images/', verbose_name='Profile picture', null=True)  

    def __str__(self):
        return self.name 

class user_profile(models.Model):
   
    EXPERIENCE = (
         ('0-3 Years','0-3 Years'),
         ('4-6 Years','4-6 Years'),
         ('7-10 Years','7-10 Years'),
         ('11+ Years',' 11+ Years'),
    )
    COUNTY = (
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
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, verbose_name="user")
    national_id = models.PositiveIntegerField(null=True, unique=True, verbose_name='National Id')
    area_of_specialization = models.ForeignKey(AreaOfSpecialization, on_delete=models.CASCADE,null=True)
    job_title = models.CharField(max_length=100, null=True)
    brief_info = models.TextField(blank=True, verbose_name='Brief Description', null=True)
    address = models.CharField(max_length=255, verbose_name='Location Address', null=True)
    phone  = models.CharField(max_length=20, verbose_name='Mobile Phone Number', null=True)
    current_location = models.CharField(max_length=20, choices=COUNTY)
    company_name = models.CharField(max_length=100, null=True)
    company_email = models.EmailField(null=True)
    image  = models.ImageField(default='empty.jpg', upload_to='images/', verbose_name='Profile picture', null=True) 
    profile_updated = models.BooleanField(default=False)
    

    def __str__(self):
        return self.user.username




