# Generated by Django 3.2.7 on 2021-11-05 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Leads', '0006_lead_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
