# Generated by Django 4.1 on 2022-11-17 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pemira_ff', '0002_candidate_cno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voteresult',
            name='candidate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pemira_ff.candidate'),
        ),
    ]
