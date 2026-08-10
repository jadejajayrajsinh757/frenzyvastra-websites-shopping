from django.contrib import admin
from django.urls import path

from jarvis import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jarvis/', views.show_jarvis, name='show_jarvis'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('mens/', views.MensPageView.as_view(), name='mens'),
]
