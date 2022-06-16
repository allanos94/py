from django.urls import path
from api import views
from .views import TeamView

urlpatterns =[
    path('hello-view/', views.HelloApiView.as_view()),
    path('teams/', TeamView.as_view(), name='teams_list'),
    path('teams/<int:id>', TeamView.as_view(), name='teams_process')
]