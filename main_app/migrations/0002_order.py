# Generated by Django 2.2 on 2021-04-24 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(choices=[('f', 'Fragile'), ('l', 'Liquid')], default='p', max_length=10)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Merchant')),
            ],
        ),
    ]