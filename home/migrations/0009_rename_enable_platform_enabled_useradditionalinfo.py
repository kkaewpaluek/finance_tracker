# Generated by Django 4.2.9 on 2024-04-15 09:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0008_platform_user_delete_customuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='platform',
            old_name='enable',
            new_name='enabled',
        ),
        migrations.CreateModel(
            name='UserAdditionalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_photo', models.ImageField(default='profile_images/teacher_default.png', upload_to='profile_images/')),
                ('user', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]