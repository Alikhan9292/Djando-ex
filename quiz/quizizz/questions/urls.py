from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index),
    path('quiz/', quiz, name='quiz'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact')
]