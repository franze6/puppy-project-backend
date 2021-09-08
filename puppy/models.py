from django.db import models

# Create your models here.
class GeneralModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    

class Contact(GeneralModel):
    last_name = models.CharField(verbose_name='Last Name', max_length=100)
    first_name = models.CharField(verbose_name='First Name', max_length=100)
    second_name = models.CharField(verbose_name='Second Name', max_length=100, blank=True)

    def __str__(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.second_name

    class Meta:
        verbose_name_plural = 'Contacts'
        verbose_name = 'Contact'