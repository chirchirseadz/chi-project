from django.contrib import admin
from . models import Message

# Register your models here.


class MessagesAdmin(admin.ModelAdmin):
    list_display = ['your_name', 'email', 'subject', 'message','date_message']
    list_filter = ['date_message']
    
admin.site.register(Message, MessagesAdmin)
