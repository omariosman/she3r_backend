from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views

from .models import Verse

urlpatterns = [
    #path('all_loans/', views.All_Loans.as_view()),
    path('get_random_verse2/', views.get_random_verse2, name="get_random_verse2"),
    #path('get_random_verse2/', views.get_random_verse.as_view()),


#    path('number_view/', views.number_view.as_view(), name="number_view"), 


]
