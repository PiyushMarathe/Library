# Generated by Django 3.1.5 on 2021-02-28 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]