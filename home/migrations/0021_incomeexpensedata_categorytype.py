# Generated by Django 4.2.9 on 2024-11-28 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_alter_incomeexpensedata_platform'),
    ]

    operations = [
        migrations.AddField(
            model_name='incomeexpensedata',
            name='categoryType',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
