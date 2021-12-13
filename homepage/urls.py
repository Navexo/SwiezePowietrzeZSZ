from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homepage, name="home"),
    path('home/<int:id>/', views.homepageid),
    path('ochrona_srodowiska/', views.ochrona, name="ochrona_srodowiska"),
]
