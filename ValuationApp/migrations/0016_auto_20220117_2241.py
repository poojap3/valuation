# Generated by Django 3.2.11 on 2022-01-17 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ValuationApp', '0015_fieldreport_fieldreport_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='fieldreport',
            name='Submission_TimeStamp',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='dob',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Created'),
        ),
    ]
