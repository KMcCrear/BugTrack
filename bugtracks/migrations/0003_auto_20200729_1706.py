# Generated by Django 3.0.8 on 2020-07-29 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracks', '0002_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='priority',
            field=models.CharField(choices=[('HIGH', 'High'), ('MEDIUM', 'Medium'), ('LOW', 'Low')], default='MEDIUM', max_length=6),
        ),
    ]
