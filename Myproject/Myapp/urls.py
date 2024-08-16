from django.urls import path
from .import views
urlpatterns = [
    path('hello/', views.say_hello),
    path('home/',views.homepage),
    path('contact/',views.contact),
    path('about/',views.about)
]