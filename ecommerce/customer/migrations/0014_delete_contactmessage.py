# Generated by Django 5.0.3 on 2024-03-20 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0013_contactmessage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactMessage',
        ),
    ]
