# Generated by Django 4.1 on 2022-11-17 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pemira_ff', '0005_alter_voteresult_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voteresult',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
