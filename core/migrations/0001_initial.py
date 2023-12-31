# Generated by Django 4.0.5 on 2022-06-28 17:22

import annoying.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=29)),
                ('area', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=27)),
                ('street', models.CharField(max_length=132)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', annoying.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='/images/default.jpg', upload_to='images/')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('category', models.CharField(choices=[('E', 'Electronics'), ('F', 'Fashion'), ('HAB', 'Health and Beauty'), ('HAG', 'House and Garden'), ('S', 'Sports'), ('A', 'Auto'), ('O', 'Others')], max_length=3)),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('description', models.TextField()),
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
