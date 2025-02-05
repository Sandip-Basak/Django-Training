# Generated by Django 5.1.3 on 2024-11-24 17:26

import home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('age', models.DecimalField(decimal_places=0, max_digits=2)),
                ('jobDescription', models.TextField()),
                ('profile_photo', models.FileField(default='static/images/media/default_user.png', upload_to=home.models.image)),
            ],
        ),
    ]
