# Generated by Django 3.2.3 on 2021-06-12 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_alter_ticket_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='completed_before',
            field=models.BooleanField(default=False),
        ),
    ]
