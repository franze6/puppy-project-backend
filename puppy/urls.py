from django.urls import path, include

from puppy.services import person_create

from .views import (
    PersonsView, 
    PersonDetailView, 
    PersonUpdateApi, 
    PersonDeleteApi,
    PersonListApi,
    PersonCreateApi,
    PersonUpdateApi,

)

app_name = 'puppy'

person_patterns = [
    #path('', PersonListApi.as_view(), name='list'),
    path('', PersonsView.as_view(), name='list'),
    path('<int:pk>/', PersonDetailView.as_view(), name='detail'),
    path('create/', PersonCreateApi.as_view(), name='create'),
    path('<int:person_id>/update/', PersonUpdateApi.as_view(), name='update'),
    path('<int:person_id>/delete/', PersonDeleteApi.as_view(), name='delete')
]

urlpatterns = [
    path('persons/', include((person_patterns, 'persons')))
    #path('person/<int:pk>/', PersonDetailView.as_view(), name='person-datail'),
    #path('person-api/<int:pk>/', PersonUpdateApi.as_view(), name='person-api'),
    #path('person-del/<int:pk>/', PersonDeleteApi.as_view(), name='person-del'),

]