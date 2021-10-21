import django_filters
from puppy.models import Person

class PersonFilter(django_filters.FilterSet):
    class Meta:
        model = Person
        fields = ('id', 'last_name')

def person_list(*, filters=None) -> Person:
    filters = filters or {}
    qs = Person.objects.all()
    return PersonFilter(filters, qs).qs

def get_person(*, id) -> Person:
    user = Person.objects.get(id=id)
    return user