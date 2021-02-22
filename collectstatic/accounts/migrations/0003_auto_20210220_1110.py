# Generated by Django 3.1.6 on 2021-02-20 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210217_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregister',
            name='fullname',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userregister',
            name='mobile',
            field=models.IntegerField(default=1, help_text='Enter 10-digit Mobile Number.'),
            preserve_default=False,
        ),
    ]