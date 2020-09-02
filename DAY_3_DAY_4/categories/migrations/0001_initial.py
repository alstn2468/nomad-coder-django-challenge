# Generated by Django 3.1.1 on 2020-09-02 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=20)),
                ('kind', models.CharField(choices=[('book', 'Book'), ('movie', 'Movie'), ('both', 'Both')], default='book', max_length=6)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]