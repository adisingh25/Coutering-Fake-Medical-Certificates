# Generated by Django 4.0.4 on 2023-02-11 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_delete_todo'),
    ]

    operations = [
        migrations.CreateModel(
            name='certificateissue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateField(auto_now_add=True)),
                ('slipno', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('docname', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('bloodgp', models.CharField(max_length=200)),
                ('height', models.CharField(max_length=200)),
                ('weight', models.CharField(max_length=200)),
                ('problem', models.CharField(max_length=200)),
                ('nextvisitafter', models.CharField(max_length=200)),
                ('HospitalName', models.CharField(max_length=200)),
            ],
        ),
    ]
