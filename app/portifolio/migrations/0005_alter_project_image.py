# Generated by Django 3.2.7 on 2021-10-01 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0004_alter_tecnology_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]