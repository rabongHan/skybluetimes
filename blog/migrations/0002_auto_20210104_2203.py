# Generated by Django 3.1.5 on 2021-01-04 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='conent',
            new_name='content',
        ),
    ]
