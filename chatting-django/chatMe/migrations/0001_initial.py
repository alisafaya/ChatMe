# Generated by Django 2.1.7 on 2019-03-30 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('media_type', models.CharField(choices=[('N', 'Not defined'), ('A', 'Audio'), ('I', 'Image'), ('V', 'Video')], default='N', max_length=1)),
                ('file', models.FileField(upload_to='chatMe_media')),
            ],
            options={
                'verbose_name': 'Media element',
            },
        ),
    ]
