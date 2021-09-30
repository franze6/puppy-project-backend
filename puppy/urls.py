from django.urls import path

from .views import PersonsView, PersonDetailView

app_name = 'puppy'

urlpatterns = [
    path('persons/', PersonsView.as_view()),
    path('person/<int:pk>/', PersonDetailView.as_view(), name='person-datail')
]