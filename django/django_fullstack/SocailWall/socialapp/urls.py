from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.index),
    path('login',views.login),
    path('reg',views.reg),
    path('welcome',views.welcome),
    path('logout',views.logout),
    path('loginz',views.loginz),
    path('addmessage',views.addmessage),
    path('addcomment/<int:id>',views.addcomment)
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)