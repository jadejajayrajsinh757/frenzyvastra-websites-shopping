from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from arynjay_store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.AboutPageView.as_view(), name='about'),
    path('mens/', views.mens_page, name='mens'),
    path('womens/', views.WomensPageView.as_view(), name='womens'),
]
