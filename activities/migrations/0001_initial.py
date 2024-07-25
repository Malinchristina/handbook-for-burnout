# Generated by Django 5.0.6 on 2024-07-25 09:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddActivity',
            fields=[
                ('activity_id', models.AutoField(primary_key=True, serialize=False)),
                ('activity_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('url_link', models.URLField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.addcategory')),
            ],
        ),
    ]
