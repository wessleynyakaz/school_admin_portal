# Generated by Django 4.2.3 on 2023-09-29 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('author', models.CharField(max_length=140)),
                ('edition', models.CharField(max_length=3)),
                ('isbn', models.CharField(max_length=255)),
                ('quantity', models.SmallIntegerField(blank=True, default=1, null=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='classroom.subject')),
            ],
            options={
                'verbose_name': 'book',
                'verbose_name_plural': 'books',
                'db_table': 'books',
            },
        ),
    ]