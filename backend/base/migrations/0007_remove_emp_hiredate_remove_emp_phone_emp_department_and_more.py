# Generated by Django 4.1.7 on 2023-05-11 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_rename_position_emp_poste_emp_hiredate_emp_salary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emp',
            name='hireDate',
        ),
        migrations.RemoveField(
            model_name='emp',
            name='phone',
        ),
        migrations.AddField(
            model_name='emp',
            name='department',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='emp',
            name='nbrAbsences',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='emp',
            name='poste',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='emp',
            name='salary',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
