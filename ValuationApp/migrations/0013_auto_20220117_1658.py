# Generated by Django 3.2.11 on 2022-01-17 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ValuationApp', '0012_remove_customuser_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fieldreport',
            name='vapp',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='vapp',
        ),
        migrations.RemoveField(
            model_name='sitevisit',
            name='issue',
        ),
        migrations.AddField(
            model_name='fieldreport',
            name='sitevisit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ValuationApp.sitevisit'),
        ),
        migrations.AddField(
            model_name='issue',
            name='field',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ValuationApp.fieldreport'),
        ),
    ]
