# Generated by Django 2.0 on 2018-03-19 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userAuth', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loaduserdatamodel',
            old_name='userInfo',
            new_name='userData',
        ),
        migrations.RemoveField(
            model_name='loaduserdatamodel',
            name='userName',
        ),
    ]
