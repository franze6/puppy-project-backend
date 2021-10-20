from puppy.models import Person, Address, Messenger, Passport
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

def address_create(
                    *, 
                    address_plain: str,
                    is_active: bool,
                    person_id: str, 
                    #company_id:str=None,
                  ) -> Address:

  obj = Address(
    address_plain=address_plain,
    is_active=is_active,
    person_id=person_id,
  )

  #obj.full_clean()
  obj.save()

  return obj

def messenger_create(
                    *, 
                    name: str,
                    is_active: bool,
                    uid: str, 
                    person_id:str,
                  ) -> Messenger:

  obj = Messenger(
    name=name,
    is_active=is_active,
    uid=uid, 
    person_id=person_id,
  )

  #obj.full_clean()
  obj.save()

  return obj

def passport_create(
                    *, 
                    series: str,
                    number: str,
                    issued_date: date, 
                    issued_by: str,
                    issued_by_code: str ,
                    person_id: str ,
                  ) -> Passport:

  obj = Passport(
    series=series,
    number=number,
    issued_date=issued_date, 
    issued_by=issued_by,
    issued_by_code=issued_by_code,
    person_id=person_id,
  )

  #obj.full_clean()
  obj.save()

  return obj
