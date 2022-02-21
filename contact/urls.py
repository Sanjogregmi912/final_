from django.urls import path
from contact import views

urlpatterns = [
    path('contactnew', views.contactnew),
    path('contactview', views.contactview)
]
