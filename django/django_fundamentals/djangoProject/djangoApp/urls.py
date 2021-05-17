from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	 
    path('cheetos',views.cheetos)  ,
    path('ninja/<name>/<age>',views.ninja),
 
]