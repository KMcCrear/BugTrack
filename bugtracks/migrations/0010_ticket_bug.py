# Generated by Django 3.0.8 on 2020-08-05 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracks', '0009_ticket_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='bug',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
