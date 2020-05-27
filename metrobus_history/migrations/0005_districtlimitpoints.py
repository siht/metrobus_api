# Generated by Django 3.0.6 on 2020-05-27 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metrobus_history', '0004_auto_20200527_0130'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistrictLimitPoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=15, max_digits=17)),
                ('longitude', models.DecimalField(decimal_places=15, max_digits=18)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metrobus_history.District')),
            ],
        ),
    ]
