# Generated by Django 3.2 on 2022-04-25 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('masterApi', '0004_constraintmaster_marketmaster_measuremaster_productgranularitymaster_spacialgranularitymaster'),
    ]

    operations = [
        migrations.AddField(
            model_name='measuremaster',
            name='marketMasterId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='masterApi.marketmaster'),
        ),
    ]