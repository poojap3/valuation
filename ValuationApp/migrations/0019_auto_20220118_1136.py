# Generated by Django 3.2.11 on 2022-01-18 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ValuationApp', '0018_issue_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='created',
        ),
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
