# Generated by Django 3.2 on 2022-04-05 06:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('masterApi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoleMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roleName', models.CharField(max_length=180)),
                ('roleCode', models.CharField(max_length=10)),
                ('createdtime', models.DateTimeField(auto_now_add=True)),
                ('updatedtime', models.DateTimeField(auto_now=True)),
                ('isActive', models.BooleanField(blank=True, default=False)),
                ('isDelete', models.BooleanField(blank=True, default=False)),
                ('updatedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessFuncMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('businessFuncName', models.CharField(max_length=180)),
                ('businessFuncCode', models.CharField(max_length=10)),
                ('createdtime', models.DateTimeField(auto_now_add=True)),
                ('updatedtime', models.DateTimeField(auto_now=True)),
                ('isActive', models.BooleanField(blank=True, default=False)),
                ('isDelete', models.BooleanField(blank=True, default=False)),
                ('updatedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]