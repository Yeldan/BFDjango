# Generated by Django 2.1.1 on 2018-10-12 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DishReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Task1.Dish')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Task1.Restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=255)),
                ('comment', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='restaurantreview',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Task1.Review'),
        ),
        migrations.AddField(
            model_name='restaurantreview',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Task1.User'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Task1.User'),
        ),
        migrations.AddField(
            model_name='dishreview',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Task1.Review'),
        ),
        migrations.AddField(
            model_name='dishreview',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Task1.User'),
        ),
        migrations.AddField(
            model_name='dish',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Task1.Restaurant'),
        ),
        migrations.AddField(
            model_name='dish',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Task1.User'),
        ),
    ]
