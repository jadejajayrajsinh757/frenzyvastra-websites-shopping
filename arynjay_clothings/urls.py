from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from arynjay_store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.AboutPageView.as_view(), name='about'),
    path('mens/', views.mens_page, name='mens'),
    path('womens/', views.WomensPageView.as_view(), name='womens'),
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup_page, name='signup'),
    path('logout/', views.logout_page, name='logout'),
    path('seller/', views.seller_dashboard, name='seller_dashboard'),
    path('seller/add-product/', views.seller_add_product, name='seller_add_product'),
    path('seller/products/', views.seller_products, name='seller_products'),
    path('seller/update-product/<int:product_id>/', views.seller_update_product, name='seller_update_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
