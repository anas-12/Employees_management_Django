# Generated by Django 4.2 on 2023-05-01 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_emp_delete_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emp',
            old_name='description',
            new_name='action',
        ),
        migrations.RenameField(
            model_name='emp',
            old_name='category',
            new_name='adresse',
        ),
        migrations.RemoveField(
            model_name='emp',
            name='image',
        ),
        migrations.RemoveField(
            model_name='emp',
            name='rating',
        ),
        migrations.AddField(
            model_name='emp',
            name='phone',
            field=models.DecimalField(decimal_places=2, max_digits=30, null=True),
        ),
    ]
