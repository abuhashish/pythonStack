from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.index),
    path('login',views.login),
    path('reg',views.reg),
    path('logout',views.logout),
    path('loginz',views.loginz),
    path('addbook',views.addbook),
    path('books',views.books),
    path('addtofav/<int:id>',views.addtofav),
    path('books/<int:id>',views.viewbook),
    path('books/unfav/<int:id>',views.unfav),
    path('delete/<int:id>',views.delete),
    path('update/<int:id>',views.update),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)