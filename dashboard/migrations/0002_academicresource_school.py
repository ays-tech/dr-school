# Generated by Django 4.1.7 on 2023-04-05 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='academicresource',
            name='school',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
