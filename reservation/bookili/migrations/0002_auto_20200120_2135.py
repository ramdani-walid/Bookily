# Generated by Django 3.0.2 on 2020-01-20 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookili', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='duree_service',
            field=models.DateTimeField(blank=True, db_column='DUREE_SERVICE', max_length=6, null=True),
        ),
    ]