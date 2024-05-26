from django.urls import path
from tusurBackSite import views

page_patterns = [
    path('index/', views.index, name='index'),
]