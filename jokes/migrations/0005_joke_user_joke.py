# Generated by Django 3.2.3 on 2021-05-23 16:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jokes', '0004_joke_add_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='joke',
            name='user_joke',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='Пользователь'),
            preserve_default=False,
        ),
    ]
