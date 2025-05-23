# Generated by Django 4.2.20 on 2025-04-23 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_stocktransaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='items_images/'),
        ),
        migrations.AddField(
            model_name='item',
            name='supplier',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='core.supplier'),
        ),
        migrations.AddField(
            model_name='item',
            name='unit',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(default=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
