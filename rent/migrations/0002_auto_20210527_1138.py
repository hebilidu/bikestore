# Generated by Django 3.2.3 on 2021-05-27 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='size',
            name='name',
            field=models.CharField(default='small', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='type',
            name='name',
            field=models.CharField(default='bike', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='created',
            field=models.DateField(auto_now_add=True, default='2021-05-27'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_date', models.DateField()),
                ('return_date', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent.customer')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daily_rate', models.FloatField()),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent.size')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent.type')),
            ],
        ),
    ]
