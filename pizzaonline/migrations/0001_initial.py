# Generated by Django 2.2.7 on 2019-11-18 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredientName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sizeName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localName', models.CharField(max_length=200)),
                ('adress', models.CharField(max_length=200)),
                ('phoneNumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('rut', models.CharField(max_length=11)),
                ('bday', models.DateField()),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('pssword', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizzaName', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='img')),
                ('price', models.IntegerField(default=0)),
                ('ingredient', models.ManyToManyField(to='pizzaonline.Ingredients')),
                ('size', models.ManyToManyField(to='pizzaonline.Size')),
            ],
        ),
    ]
