# Generated by Django 3.2.11 on 2022-01-18 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ValuationApp', '0017_remove_issue_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created'),
        ),
    ]