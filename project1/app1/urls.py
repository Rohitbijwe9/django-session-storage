from django.urls import path
from .views import *



urlpatterns=[
    path('add/',ProductView.as_view()),
    path('show/',ProductView.as_view()),
    path('update/<int:pk>/',ProductView.as_view()),
    path('pupdate/<int:pk>/',ProductView.as_view()),
    path('del/<int:pk>/',ProductView.as_view())

]