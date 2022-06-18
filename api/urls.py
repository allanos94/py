from django.urls import path
from api import views
from .views import team_api_view
from .views import team_detail_view
from .views import player_api_view
from .views import player_detail_view
from .views import staff_api_view
from .views import staff_detail_view
from django.urls import path, include
from .views import team_api_view, player_api_count, team_more_players
from .views import test_age_older, starting_api_count, team_api_count


urlpatterns =[
    path('teams/', team_api_view, name='teams_list'),
    path('teams/<int:pk>', team_detail_view, name='team_view'),
    path('players/', player_api_view, name='players_list'),
    path('players/<int:pk>', player_detail_view, name='player_view'),
    path('staff/', staff_api_view, name='staff_list'),
    path('staff/<int:pk>', staff_detail_view, name='staff_view'),
    path('math/howmanyteams', team_api_count, name='team_math_view'),
    path('math/howmanyplayers', player_api_count, name='player_math_view'),
    path('math/oldestplayer', test_age_older, name='oldest_player_view'),
    path('math/starting', starting_api_count, name='starting_players_view'),
    path('math/moreplayers', team_more_players, name='starting_players_view'),
]