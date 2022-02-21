from django.urls import path
from customer import views


urlpatterns = [
    path("", views.homepage, name='home' ),
    path("login", views.login,name="login"),
    path("registration", views.registration,name="registration"),
    path("dashboard", views.dashboard,name="dashboard"),
    path("view", views.view,name="view"),
    path("customer_create", views.customer_create,name="customer_create"),
    path("customer_edit/<int:p_id>",views.customer_edit,name="customer_edit"),
    path("customer_edit/customer_update/<int:p_id>",views.customer_update,name="customer_update"),
    path("customer_delete/<int:p_id>",views.customer_delete,name="customer_delete"),
   
    
    

]
