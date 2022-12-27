from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path('', views.landingpage, name='login'),
    path('', lambda req: redirect('/debitcreditcapital/')),
    path('CustomerView', views.customer, name='customer'),
    path('EmployeeView',views.addcustomer, name='addcustomer'),
    path('Authview', views.loginvalidation, name='loginvalidation'),
    path('Logout', views.logout, name='logout'),
    path('Confirmation', views.addconfirmation, name='addconfirmation')
]