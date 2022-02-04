from django.urls import path
from django.urls import path
from . import views


app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),path('dashboard', views.index, name='index'),
    path('about', views.about, name='about'), path('terms', views.terms, name='terms'),

]
