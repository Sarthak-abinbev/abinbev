# Generated by Django 3.2 on 2022-04-25 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('masterApi', '0005_measuremaster_marketmasterid'),
        ('expRepo', '0004_rename_levelpercentageassign_levels_levelpercentageassign'),
    ]

    operations = [
        migrations.AddField(
            model_name='experimentrepo',
            name='marketMasterId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='masterApi.measuremaster'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='experimentrepo',
            name='productGranularityMasterId',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='masterApi.productgranularitymaster'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='experimentrepo',
            name='spacialGranularityMasterId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='masterApi.spacialgranularitymaster'),
            preserve_default=False,
        ),
    ]