from django.urls import path
from . import views

urlpatterns = [
    path('accounts/signup/', views.signup, name='signup'),
    path('', views.Home,name='Home'),
    path('profile/', views.index,name='index'),
    path('about/', views.about,name='about'),
    path('addPersonFitness/<int:user_id>', views.add_personfitness, name='add_person_fitness')
]
  