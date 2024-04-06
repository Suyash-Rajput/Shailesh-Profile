from . import views
from django.urls import path


urlpatterns= [
    path("home.html", views.home, name = 'home'),
    path('Contract.html', views.contract_page, name='contract_page'),   
    path('Hobbies.html', views.hobbie_page, name='hobbie_page'), 
    path('send-email', views.send_email, name='send_email'),
]