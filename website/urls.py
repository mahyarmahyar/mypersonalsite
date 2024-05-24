from django.urls import path
from .views import *

app_name = 'website'

urlpatterns = [
    path('', index_view, name='index'),
    path('contact/', contact_view, name='contact'),
]
