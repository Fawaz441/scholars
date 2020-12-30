from django.urls import path
from .views import add_bulk_university
app_name = 'utils'

urlpatterns = [
    path('add_bulk_unis',add_bulk_university,name='add_bulk_universities'),
]