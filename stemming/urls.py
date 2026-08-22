from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Halaman Utama
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('process/', views.stemming_process, name='stemming_process'),
    path('stemming/', views.stemming_process, name='stemming'),
    path('export/', views.export_csv, name='export'),
]