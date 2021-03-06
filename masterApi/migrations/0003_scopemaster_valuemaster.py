# Generated by Django 3.2 on 2022-04-13 08:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('masterApi', '0002_businessfuncmaster_rolemaster'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScopeMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scopeFilterName', models.CharField(max_length=180)),
                ('scopeFilterCode', models.CharField(max_length=10)),
                ('createdtime', models.DateTimeField(auto_now_add=True)),
                ('updatedtime', models.DateTimeField(auto_now=True)),
                ('isActive', models.BooleanField(blank=True, default=False)),
                ('isDelete', models.BooleanField(blank=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ValueMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valueFilterName', models.CharField(max_length=180)),
                ('valueFilterCode', models.CharField(max_length=10)),
                ('createdtime', models.DateTimeField(auto_now_add=True)),
                ('updatedtime', models.DateTimeField(auto_now=True)),
                ('isActive', models.BooleanField(blank=True, default=False)),
                ('isDelete', models.BooleanField(blank=True, default=False)),
                ('scopeMasterid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='masterApi.scopemaster')),
                ('updatedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
