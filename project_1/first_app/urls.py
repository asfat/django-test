from django.urls import path
from . import views

urlpatterns = [
    path('courses/',views.courses),
    path('',views.home),
    path('contact/',views.contact),
    path('1/2/3/',views.multidirectories),
]