# Generated by Django 4.0.4 on 2022-06-03 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_clienturl_clientpass_clienturl_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staffpass', models.CharField(max_length=20)),
                ('staffname', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('clientname', models.CharField(max_length=200, null=True)),
                ('staffurl', models.CharField(max_length=500)),
            ],
        ),
    ]