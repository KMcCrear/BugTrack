# Generated by Django 3.0.8 on 2020-08-05 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracks', '0007_ticket_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='owner',
        ),
    ]
