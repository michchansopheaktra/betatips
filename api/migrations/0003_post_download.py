# Generated by Django 4.2 on 2025-07-19 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_post_ads_1_post_ads_2_post_ads_3_post_ads_4_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='download',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
