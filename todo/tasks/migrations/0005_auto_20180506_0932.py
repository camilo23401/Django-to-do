# Generated by Django 2.0.5 on 2018-05-06 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20180506_0853'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Username',
        ),
        migrations.AddField(
            model_name='task',
            name='username',
            field=models.CharField(default='omkar', max_length=50, unique=True, null=True),
            preserve_default=False,
        ),
    ]
