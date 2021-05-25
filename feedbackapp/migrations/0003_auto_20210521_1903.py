# Generated by Django 3.0.5 on 2021-05-21 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbackapp', '0002_facultyfeedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='facultyfeedback',
            name='course',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='facultyfeedback',
            name='department',
            field=models.CharField(max_length=30),
        ),
    ]
