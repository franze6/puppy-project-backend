from django.urls import path, include

from .views import (
    PersonDetailView, 
    PersonUpdateApi, 
    PersonDeleteApi,
    PersonListApi,
    PersonCreateApi,
    PersonUpdateApi,
    PersonDetailApi,
    AddressCreateApi,
    AddressDeleteApi,
    MessengerCreateApi,
    MessengerDeleteApi,
    PassportCreateApi,
    PassportDeleteApi,
)

app_name = 'puppy'

person_patterns = [
    path('', PersonListApi.as_view(), name='list'),
    path('<int:person_id>/', PersonDetailApi.as_view(), name='detail'),
    path('create/', PersonCreateApi.as_view(), name='create'),
    path('<int:person_id>/update/', PersonUpdateApi.as_view(), name='update'),
    path('<int:person_id>/delete/', PersonDeleteApi.as_view(), name='delete')
]

address_patterns = [
    #path('', PersonListApi.as_view(), name='list'),
    #path('', PersonsView.as_view(), name='list'),
    #path('<int:pk>/', PersonDetailView.as_view(), name='detail'),
    path('create/', AddressCreateApi.as_view(), name='create'),
    #path('<int:person_id>/update/', PersonUpdateApi.as_view(), name='update'),
    path('<int:id>/delete/', AddressDeleteApi.as_view(), name='delete')
]

messenger_patterns = [
    #path('', PersonListApi.as_view(), name='list'),
    #path('', PersonsView.as_view(), name='list'),
    #path('<int:pk>/', PersonDetailView.as_view(), name='detail'),
    path('create/', MessengerCreateApi.as_view(), name='create'),
    #path('<int:person_id>/update/', PersonUpdateApi.as_view(), name='update'),
    path('<int:id>/delete/', MessengerDeleteApi.as_view(), name='delete')
]

passport_patterns = [
    #path('', PersonListApi.as_view(), name='list'),
    #path('', PersonsView.as_view(), name='list'),
    #path('<int:pk>/', PersonDetailView.as_view(), name='detail'),
    path('create/', PassportCreateApi.as_view(), name='create'),
    #path('<int:person_id>/update/', PersonUpdateApi.as_view(), name='update'),
    path('<int:id>/delete/', PassportDeleteApi.as_view(), name='delete')
]

urlpatterns = [
    path('persons/', include((person_patterns, 'persons'))),
    path('addresses/', include((address_patterns, 'addresses'))),
    path('messengers/', include((messenger_patterns, 'messengers'))),
    path('passports/', include((passport_patterns, 'passports'))),
    #path('person/<int:pk>/', PersonDetailView.as_view(), name='person-datail'),
    #path('person-api/<int:pk>/', PersonUpdateApi.as_view(), name='person-api'),
    #path('person-del/<int:pk>/', PersonDeleteApi.as_view(), name='person-del'),

]