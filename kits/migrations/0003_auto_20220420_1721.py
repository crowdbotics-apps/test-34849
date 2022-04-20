# Generated by Django 2.2.26 on 2022-04-20 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kits', '0002_auto_20220420_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionDeviceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='CollectionDeviceTypeSkus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_device_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collectiondevicetypeskus_collection_device_type', to='kits.CollectionDeviceType')),
                ('sku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collectiondevicetypeskus_sku', to='kits.Sku')),
            ],
        ),
        migrations.AddField(
            model_name='collectiondevice',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='collectiondevice_type', to='kits.CollectionDeviceType'),
        ),
    ]
