# Generated by Django 4.0.4 on 2023-02-11 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_certificate_ticketid'),
    ]

    operations = [
        migrations.CreateModel(
            name='dwonloadCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slip_id', models.IntegerField(unique=True)),
            ],
        ),
    ]
