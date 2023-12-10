from app2.views import *
from django.urls import path
app_name='baap'

urlpatterns=[

    path('india/',india,name='india'),
]