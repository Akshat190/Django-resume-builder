# Generated by Django 4.0 on 2022-08-14 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_profile_avator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avator',
            field=models.ImageField(default='profile/avator.png', null=True, upload_to='profile/'),
        ),
    ]