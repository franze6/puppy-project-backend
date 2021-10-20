from puppy.models import Person
from datetime import date

def person_create(
                    *, 
                    last_name: str,
                    first_name: str,
                    second_name:str=None, 
                    birth_date:date=None,
                    tax_id:str=None,
                    insurance_number:str=None,
                    gender:str=None,
                    description:str=None,
                  ) -> Person:

  obj = Person(
    last_name=last_name,
    first_name=first_name,
    second_name=second_name, 
    birth_date=birth_date,
    tax_id=tax_id,
    insurance_number=insurance_number,
    gender=gender,
    description=description,
  )

  #obj.full_clean()
  obj.save()

  return obj

def person_update(
                    id: str,
                    *,
                    last_name: str=None,
                    first_name: str=None,
                    second_name:str=None, 
                    birth_date:date=None,
                    tax_id:str=None,
                    insurance_number:str=None,
                    gender:str=None,
                    description:str=None,
                  ) -> None:
    kwargs = dict(locals())
    update_fields = {k: v for k, v in kwargs.items() if v is not None and k !='id'}
    Person.objects.filter(id=id).update(**update_fields)

    return None

def person_delete(id: str) -> None:
    Person.objects.filter(id=id).delete()
    return None