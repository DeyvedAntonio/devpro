from django.contrib import admin  # noqa F401
from django.urls import path


from projeto.core import views


app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
]
