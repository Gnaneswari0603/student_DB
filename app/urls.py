from django.urls import path
from.import views

urlpatterns=[
    path('',views.register),
    path('1',views.display,name="display"),
    path('2/<int:id>',views.single_data,name="single"),
    path('3/<int:pk>',views.edit,name="edit"),
    path('4/<int:id>',views.delete_data,name="delete"),
]