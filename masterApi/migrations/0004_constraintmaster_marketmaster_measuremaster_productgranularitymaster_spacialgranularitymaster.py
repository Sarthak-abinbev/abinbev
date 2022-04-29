# Generated by Django 3.2 on 2022-04-19 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterApi', '0003_scopemaster_valuemaster'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConstraintMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('constraintName', models.CharField(max_length=180)),
                ('constraintCode', models.CharField(max_length=10)),
                ('createdtime', models.DateTimeField(auto_now_add=True)),
                ('updatedtime', models.DateTimeField(auto_now=True)),
                ('isActive', models.BooleanField(blank=True, default=False)),
                ('isDelete', models.BooleanField(blank=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MarketMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marketName', models.CharField(max_length=180)),
                ('marketCode', models.CharField(max_length=10)),
                ('createdtime', models.DateTimeField(auto_now_add=True)),
                ('updatedtime', models.DateTimeField(auto_now=True)),
                ('isActive', models.BooleanField(blank=True, default=False)),
                ('isDelete', models.BooleanField(blank=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MeasureMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measureName', models.CharField(max_length=180)),
                ('measureCode', models.CharField(max_length=10)),
                ('createdtime', models.DateTimeField(auto_now_add=True)),
                ('updatedtime', models.DateTimeField(auto_now=True)),
                ('isActive', models.BooleanField(blank=True, default=False)),
                ('isDelete', models.BooleanField(blank=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProductGranularityMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productGranularityfilterName', models.CharField(max_length=180)),
                ('productGranularityfilterCode', models.CharField(max_length=10)),
                ('createdtime', models.DateTimeField(auto_now_add=True)),
                ('updatedtime', models.DateTimeField(auto_now=True)),
                ('isActive', models.BooleanField(blank=True, default=False)),
                ('isDelete', models.BooleanField(blank=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SpacialGranularityMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spacialGranularityfilterName', models.CharField(max_length=180)),
                ('spacialGranularityfilterCode', models.CharField(max_length=10)),
                ('createdtime', models.DateTimeField(auto_now_add=True)),
                ('updatedtime', models.DateTimeField(auto_now=True)),
                ('isActive', models.BooleanField(blank=True, default=False)),
                ('isDelete', models.BooleanField(blank=True, default=False)),
            ],
        ),
    ]