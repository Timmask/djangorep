# Generated by Django 2.2.24 on 2021-12-02 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20211130_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='products',
        ),
        migrations.AddField(
            model_name='card',
            name='bike',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.Bike'),
        ),
    ]
