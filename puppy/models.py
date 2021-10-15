#TODO Проработать Cascade Delete
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


class Company(GeneralModel):
  name = models.CharField(verbose_name='Название', max_length=200, null=True, blank=True)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name_plural = 'Компании'
    verbose_name = 'Компания'

class Project(GeneralModel):
  name = models.CharField(verbose_name='Название', max_length=200, null=True, blank=True)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name_plural = 'Проекты'
    verbose_name = 'Проект'
class Career(GeneralModel):
  person_id = models.ForeignKey(Person, related_name='career', on_delete=CASCADE)
  company_id = models.ForeignKey(Company, related_name='career', on_delete=CASCADE)
  project_id = models.ForeignKey(Project, related_name='career', on_delete=CASCADE)
  start_date = models.DateField(verbose_name='Дата начала', null=True, blank=True)
  end_date = models.DateField(verbose_name='Дата окончания', null=True, blank=True)
  job_title = models.CharField(verbose_name='Должность', max_length=200, null=True, blank=True)
  role = models.CharField(verbose_name='Роль', max_length=200, null=True, blank=True)

  def __str__(self):
    return self.job_title

  class Meta:
    verbose_name_plural = 'Карьерный путь'
    verbose_name = 'Карьерный путь'



  
class Address(GeneralModel):
  address_plain = models.CharField(verbose_name='Адрес', max_length=1000, null=True, blank=True)
  is_active = models.BooleanField(verbose_name='Действующий')
  person_id = models.ForeignKey(Person,  related_name='address', on_delete=CASCADE, null=True, blank=True)
  company_id = models.ForeignKey(Company, related_name='address', on_delete=CASCADE, null=True, blank=True)

  def __str__(self):
    return self.address_plain

  class Meta:
    verbose_name_plural = 'Адреса'
    verbose_name = 'Адрес'
