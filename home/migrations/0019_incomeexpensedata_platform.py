# Generated by Django 4.2.9 on 2024-05-26 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_rename_savingdata_assetdata_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='incomeexpensedata',
            name='platform',
            field=models.CharField(default='SCB Account + Cash', max_length=100),
            preserve_default=False,
        ),
    ]