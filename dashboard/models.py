from django.db import models

# Create your models here.

# Landing page messages

class Message(models.Model):
    your_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    subject = models.CharField(max_length=100, null=True)
    message = models.TextField(blank=False)
    date_message = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.subject}'

