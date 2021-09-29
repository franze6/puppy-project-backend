from django.db import models
from datetime import date

# Create your models here.
class GeneralModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    

class Contact(GeneralModel):
    last_name = models.CharField(verbose_name='Last Name', max_length=100)
    first_name = models.CharField(verbose_name='First Name', max_length=100)
    second_name = models.CharField(verbose_name='Second Name', max_length=100, blank=True)
    birth_date = models.DateField(verbose_name='Birth Date', default=date.today)
    tax_id = models.PositiveIntegerField(verbose_name='INN', null=True)
    insurance_number = models.PositiveIntegerField(verbose_name='SNILS', null=True)
    gender = models.CharField(verbose_name='Gender', max_length=15, null=True)
    description = models.CharField(verbose_name='Description', max_length=255, null=True)

    def __str__(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.second_name

    class Meta:
        verbose_name_plural = 'Persons'
        verbose_name = 'Person'