from django.urls import path

from .views import ContactsView

app_name = 'puppy'

urlpatterns = [
    path('contacts/', ContactsView.as_view())
]