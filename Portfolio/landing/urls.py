from django.urls import path
from .views import *
from landing.views import Index, Work

urlpatterns = [
    #path('', index, name="home"),
    path('', Index.as_view(), name='index'),
    path('work/<int:pk>/', Work.as_view(), name='view_work'),
    path('works/', Works.as_view(), name='works')
]