# Generated by Django 2.2.5 on 2019-09-14 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('species', models.CharField(max_length=50)),
                ('dimensions', models.FloatField()),
                ('price', models.FloatField()),
                ('status', models.CharField(choices=[('PENDING', 'Transaction pending'), ('PAID', 'Invoice paid'), ('COMPLETE', 'Transaction complete')], default='PENDING', max_length=10)),
                ('notes', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Plywood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('species', models.CharField(max_length=50)),
                ('dimensions', models.FloatField()),
                ('price', models.FloatField()),
                ('status', models.CharField(choices=[('PENDING', 'Transaction pending'), ('PAID', 'Invoice paid'), ('COMPLETE', 'Transaction complete')], default='PENDING', max_length=10)),
                ('notes', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
