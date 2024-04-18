# Generated by Django 5.0.4 on 2024-04-18 12:24

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]