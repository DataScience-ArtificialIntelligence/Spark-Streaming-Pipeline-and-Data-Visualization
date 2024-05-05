# Generated by Django 3.1.1 on 2020-09-27 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='event_message_detail_agg_tbl',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('event_country_code', models.CharField(max_length=100)),
                ('event_country_name', models.CharField(max_length=100)),
                ('event_city_name', models.CharField(max_length=20)),
                ('event_server_status_color_name', models.CharField(max_length=50)),
                ('event_server_status_severity_level', models.CharField(max_length=50)),
                ('total_estimated_resolution_time', models.IntegerField()),
                ('total_message_count', models.IntegerField()),
            ],
        ),
    ]