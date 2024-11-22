from django.urls import path
from.import views

urlpatterns=[
    path('',views.home),
    path('phonebook/',views.addphone, name='addphone'),  
    path('phonebook/display/',views.display, name='display_contacts'),
   path('update/', views.update, name='update'),  # Ensure this is correct
    path('phonebook/display/delete/', views.delete, name='delete_contact'),  # Ensure this is present
     path('phonebook/display/update/', views.update, name='update_contact'),
]
