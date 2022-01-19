# Generated by Django 3.1.3 on 2022-01-08 04:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_id', models.CharField(blank=True, max_length=10, null=True)),
                ('team_name', models.CharField(blank=True, max_length=100, null=True)),
                ('team_email', models.EmailField(blank=True, max_length=50, null=True)),
                ('team_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('team_password', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_id', models.CharField(blank=True, max_length=50, null=True)),
                ('file_no', models.CharField(blank=True, max_length=50, null=True)),
                ('purpose', models.CharField(blank=True, max_length=200, null=True)),
                ('property_name', models.CharField(blank=True, max_length=100, null=True)),
                ('property_address', models.CharField(blank=True, max_length=500, null=True)),
                ('property_status', models.CharField(blank=True, max_length=50, null=True)),
                ('owner_name', models.CharField(blank=True, max_length=100, null=True)),
                ('owner_address', models.CharField(blank=True, max_length=500, null=True)),
                ('owner_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('owner_email', models.EmailField(blank=True, max_length=50, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created')),
            ],
        ),
        migrations.CreateModel(
            name='SiteVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_visit_id', models.CharField(blank=True, max_length=20, null=True)),
                ('site_visit_location', models.CharField(blank=True, max_length=200, null=True)),
                ('site_visit_date', models.CharField(blank=True, max_length=20, null=True)),
                ('site_visit_comments', models.CharField(blank=True, max_length=2000, null=True)),
                ('vapp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ValuationApp.vapp')),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_id', models.CharField(blank=True, max_length=20, null=True)),
                ('issue_name', models.CharField(blank=True, max_length=200, null=True)),
                ('issue_comments', models.CharField(blank=True, max_length=2000, null=True)),
                ('vapp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ValuationApp.vapp')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=20, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]