from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index),
    path('add',views.add),
    path('get/<int:id>',views.get),
    path('delete/<int:id>',views.delete),
    path('update/<id>',views.update),
    
]
