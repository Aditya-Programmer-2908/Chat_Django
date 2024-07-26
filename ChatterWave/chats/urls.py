# urls.py
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from chats import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('room/<str:room>/', views.room, name='room'),
    path('checkview/', views.checkview, name='checkview'),
    path('send/', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
