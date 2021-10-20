from puppy.models import Person


from puppy.models import Person

def person_list() -> Person:
    return Person.objects.all()