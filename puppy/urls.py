from django.urls import path

from .views import PersonsView

app_name = 'puppy'

urlpatterns = [
    path('persons/', PersonsView.as_view())
]