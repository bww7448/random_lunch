# Generated by Django 3.0.3 on 2020-07-24 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0002_auto_20200722_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_loc_add',
            field=models.CharField(default='우림라이온스밸리A', max_length=500),
        ),
    ]
