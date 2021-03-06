# Generated by Django 3.0.5 on 2021-03-29 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ViewBooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BookName', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('image', models.FileField(upload_to='')),
                ('new', models.BooleanField()),
                ('userid', models.CharField(max_length=50)),
            ],
        ),
    ]
