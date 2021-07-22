# Generated by Django 3.2.5 on 2021-07-22 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_carton_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carton', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='todo_app.carton')),
                ('products', models.ManyToManyField(blank=True, null=True, to='todo_app.Product')),
            ],
        ),
    ]
