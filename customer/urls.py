from django.urls import path
from customer import views


urlpatterns = [
    path("", views.homepage, name='home'),
    path("login", views.login),
    path("registration", views.registration),
    path("dashboard", views.dashboard),
    path("view", views.view),
    path("customer_create", views.customer_create),
    path("customer_edit/<int:p_id>",views.customer_edit),
    path("customer_edit/customer_update/<int:p_id>",views.customer_update),
    path("customer_delete/<int:p_id>",views.customer_delete),
   
    
    

]
