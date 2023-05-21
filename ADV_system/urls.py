from django.urls import path
from . import views


urlpatterns = [
    path('', views.viewAds, name='ads'),
    path('register/', views.addAd, name='reg')
]
