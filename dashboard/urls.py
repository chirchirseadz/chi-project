from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('index/', views.index, name='homepage'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contact, name='contact'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('news_and_notices/', views.news_and_notices, name='news_and_notices'),
    
    # path('blog/', views.blog, name='blog' ),
    # path('admin_assistant/', views.admin_assistant, name='admin_assistant'),
    # path('clerk_data_entry/', views.clerk_data_entry, name='clerk_data_entry'),
    # path('it_spacialist/', views.it_spacialist, name='it_spacialist'),
    # path('hospitality/', views.hospitality, name='hospitality'),
    # path('customer_care/', views.customer_care, name='customer_care'),
    # path('hospitality_wait_staff/', views.hospitality_wait_staff, name='hospitality_wait_staff'),
    
    
    
    
]
