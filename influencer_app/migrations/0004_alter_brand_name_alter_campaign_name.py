# Generated by Django 4.2.6 on 2023-11-07 11:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("influencer_app", "0003_alter_brand_name_alter_brand_product_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="brand",
            name="name",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="campaign",
            name="name",
            field=models.CharField(max_length=100),
        ),
    ]
