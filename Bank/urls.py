from django.urls import path
from . import views 

urlpatterns=[
    path('',views.home, name='home'),
    path('account',views.account, name='account'),
    path('loans',views.loans, name='loans'),
    path('cards',views.cards, name='cards'),
]