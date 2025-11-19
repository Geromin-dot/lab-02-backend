from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage_view , name='homepage_html'),
    path('login/', views.login_view , name='login_html'),
    path('admin/', admin.site.urls),
    path('registration/', include('registration.urls')), 


]