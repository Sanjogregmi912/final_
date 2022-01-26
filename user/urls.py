from django.urls import path
from user import views

urlpatterns = [
    path('user_view', views.user_view),
    path('user_create', views.user_create),
    path('user_edit/<int:p_id>', views.user_edit),
    path('user_edit/user_update/<int:p_id>', views.user_update),
    path('user_delete/<int:p_id>', views.user_delete),

]
