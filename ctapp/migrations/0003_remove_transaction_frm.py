# Generated by Django 3.1.4 on 2021-01-02 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ctapp', '0002_auto_20210102_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='frm',
        ),
    ]
