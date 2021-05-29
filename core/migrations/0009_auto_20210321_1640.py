# Generated by Django 2.2.14 on 2021-03-21 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_market_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='market',
            name='parent',
        ),
        migrations.AddField(
            model_name='item',
            name='market',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='core.Market'),
        ),
    ]
