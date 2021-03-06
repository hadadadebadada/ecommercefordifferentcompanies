# Generated by Django 2.2.14 on 2021-03-19 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210319_1502'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestModel',
        ),
        migrations.AddField(
            model_name='market',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='market',
            name='branch',
            field=models.CharField(choices=[('E', 'Elektro'), ('S', 'Spielwaren'), ('L', 'Lebensmittel')], max_length=1),
        ),
    ]
