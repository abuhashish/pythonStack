from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index),
    path('check',views.check),
    path('again',views.again),
    path('leaderboard',views.board),
    
]
