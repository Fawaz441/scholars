from django.urls import path
from .views import (Universities,UniversityCourses,PqsView,MaterialsView,
                    CreateMaterial,CreatePQ,Adverts,admin_view,approve_advert,
                    approve_advert,approve_pq,approve_material,delete_advert,delete_pq,
                    delete_material,load_courses,HomePage)

app_name = 'scholars'

urlpatterns = [
    path('',HomePage.as_view(),name='homepage'),
    path('universities',Universities.as_view(),name = 'universities'),
    path('<slug>/courses',UniversityCourses.as_view(),name = 'courses'),
    path('materials',MaterialsView.as_view(),name = 'materials'),
    path('<slug>/past-questions',PqsView.as_view(),name = 'pqs'),
    path('add-material',CreateMaterial.as_view(),name = 'add_material'),
    path('add-past-question',CreatePQ.as_view(),name = 'add_pq'),
    path('products/',Adverts.as_view(),name = 'adverts'),
    # Admin 
    path('approve-advert/<slug>',approve_advert,name = 'approve_advert'),
    path('approve-pq/<slug>',approve_pq,name = 'approve_pq'),
    path('approve-material/<slug>',approve_material,name = 'approve_material'),
    path('delete-advert/<slug>',delete_advert,name = 'delete_advert'),
    path('delete-pq/<slug>',delete_pq,name = 'delete_pq'),
    path('delete-material/<slug>',delete_material,name = 'delete_material'),
    path('agba',admin_view,name='agba'),
    # Dropdowns
    path('ajax/load-courses',load_courses,name='ajax_load_courses'),
]
