# Generated by Django 3.2.11 on 2022-01-13 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ValuationApp', '0006_auto_20220113_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='fieldreport',
            name='fieldreport_comment',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
