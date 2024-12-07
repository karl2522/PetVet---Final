# Generated by Django 5.1.1 on 2024-12-07 14:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appointments', '0001_initial'),
        ('pet_registration', '0001_initial'),
        ('registration_login', '0001_initial'),
        ('veterinarians', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registration_login.profile'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='pet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='pet_registration.pet'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='veterinarian',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='appointments', to='veterinarians.veterinarianprofile'),
        ),
    ]
