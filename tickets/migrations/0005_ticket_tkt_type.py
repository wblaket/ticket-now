# Generated by Django 3.1.7 on 2021-03-24 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_ticket_tkt_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='tkt_type',
            field=models.CharField(choices=[('INCIDENT', 'Incident'), ('REQUEST', 'Request'), ('CHANGE', 'Change'), ('PROBLEM', 'Problem')], default='INCIDENT', max_length=10),
        ),
    ]