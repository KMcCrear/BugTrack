# Generated by Django 3.0.8 on 2020-08-01 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracks', '0004_auto_20200729_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='ticket_progress',
            field=models.CharField(choices=[('In progress', 'In progress'), ('Completed', 'Completed')], default='In progress', max_length=20),
        ),
    ]
