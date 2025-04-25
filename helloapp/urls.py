from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_json),
    path('html/', views.hello_html),
]

