# Generated by Django 4.2.3 on 2023-09-29 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FundRaising',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('earnings', models.PositiveSmallIntegerField(default=0, verbose_name='earning')),
            ],
            options={
                'verbose_name': 'fund_raising',
                'verbose_name_plural': 'fund_raisings',
                'db_table': 'fund_raisings',
            },
        ),
    ]
