# Generated by Django 4.1.5 on 2023-04-14 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='urun',
            name='resim',
            field=models.FileField(null=True, upload_to='urunler/'),
        ),
    ]
