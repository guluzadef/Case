# Generated by Django 3.2.5 on 2021-07-22 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carton',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, related_name='products', to='todo_app.Product'),
        ),
    ]