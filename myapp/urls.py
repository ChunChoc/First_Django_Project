from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('select/', views.select, name='select'),
    path('select/patient', views.patient, name='paciente'),
    path('select/doctor', views.doctor, name='medico')
]