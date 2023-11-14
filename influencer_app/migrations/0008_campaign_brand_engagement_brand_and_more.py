# Generated by Django 4.2.6 on 2023-11-08 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("influencer_app", "0007_alter_brand_name_alter_campaign_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="campaign",
            name="brand",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="influencer_app.brand",
            ),
        ),
        migrations.AddField(
            model_name="engagement",
            name="brand",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="influencer_app.brand",
            ),
        ),
        migrations.AddField(
            model_name="incomestatement",
            name="brand",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="influencer_app.brand",
            ),
        ),
    ]
