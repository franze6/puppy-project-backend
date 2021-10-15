from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone

# Create your models here.
class GeneralModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    

class Person(GeneralModel):
    last_name = models.CharField(verbose_name='Last Name', max_length=100)
    first_name = models.CharField(verbose_name='First Name', max_length=100)
    second_name = models.CharField(verbose_name='Second Name', max_length=100, null=True, blank=True)
    birth_date = models.DateField(verbose_name='Birth Date', null=True)
    tax_id = models.CharField(verbose_name='INN', max_length=20, null=True, blank=True)
    insurance_number = models.CharField(verbose_name='SNILS', max_length=20, null=True, blank=True)
    gender = models.CharField(verbose_name='Gender', max_length=15, null=True, blank=True)
    description = models.TextField(verbose_name='Description', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.last_name + ' ' + self.first_name

    class Meta:
        verbose_name_plural = 'Persons'
        verbose_name = 'Person'

class Address(GeneralModel):
  address_plain = models.CharField(verbose_name='Адрес', max_length=1000, null=True, blank=True)
  is_active = models.BooleanField(verbose_name='Действующий')
  person_id = models.ForeignKey(Person, on_delete=CASCADE)

  def __str__(self):
    return self.address_plain

  class Meta:
    verbose_name_plural = 'Адреса'
    verbose_name = 'Адрес'
