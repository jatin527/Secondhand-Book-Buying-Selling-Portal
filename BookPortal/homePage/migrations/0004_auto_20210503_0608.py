# Generated by Django 3.0.5 on 2021-05-03 06:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0003_cart_orders_review'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.AddField(
            model_name='viewbooks',
            name='audio',
            field=models.FileField(null=True, upload_to='audio'),
        ),
        migrations.AddField(
            model_name='viewbooks',
            name='status',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='viewbooks',
            name='upload_date',
            field=models.DateField(auto_now=True),
        ),
    ]
