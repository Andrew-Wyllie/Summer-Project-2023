from django.urls import path
from gig import views

app_name = 'gig'

urlpatterns = [
    path('', views.findgigs, name='findgigs'),
    path('test/', views.test, name='test')
]