# Generated by Django 4.2.11 on 2024-05-05 13:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coffeeshop', '0002_review_delete_core'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='content',
            field=models.TextField(default=datetime.datetime(2024, 5, 5, 13, 10, 4, 946140, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to=settings.AUTH_USER_MODEL),
        ),
    ]
