from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('personDisplayData', views.person_info, name='person_info')
]
