from django.urls import path
from games import views

urlpatterns = [
    path('games_view',views.games_view),
    path('games_add',views.games_add),
    path('games_edit/<int:p_id>',views.games_edit),
    path('games_update/<int:p_id>',views.games_update),
    path('games_delete/<int:p_id>',views.games_delete),
    path('games_all',views.games_all),
    path('games_rpg',views.games_rpg),
    path('games_battle',views.games_battle),
    path('games_board',views.games_board),
   
    
]

