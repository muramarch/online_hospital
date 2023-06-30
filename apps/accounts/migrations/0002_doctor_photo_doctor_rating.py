# Generated by Django 4.2.2 on 2023-06-30 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='doctor',
            name='rating',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
    ]
