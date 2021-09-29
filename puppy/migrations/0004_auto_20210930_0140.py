# Generated by Django 3.2.7 on 2021-09-29 22:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('puppy', '0003_auto_20210929_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('generalmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='puppy.generalmodel')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('second_name', models.CharField(max_length=100, null=True, verbose_name='Second Name')),
                ('birth_date', models.DateField(default=datetime.date.today, verbose_name='Birth Date')),
                ('tax_id', models.PositiveIntegerField(null=True, verbose_name='INN')),
                ('insurance_number', models.PositiveIntegerField(null=True, verbose_name='SNILS')),
                ('gender', models.CharField(max_length=15, null=True, verbose_name='Gender')),
                ('description', models.TextField(max_length=255, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Persons',
            },
            bases=('puppy.generalmodel',),
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]