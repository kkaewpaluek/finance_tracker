# Generated by Django 4.2.9 on 2024-09-21 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_incomeexpensedata_platform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomeexpensedata',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.platformcategory'),
        ),
    ]