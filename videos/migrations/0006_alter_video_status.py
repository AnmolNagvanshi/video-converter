# Generated by Django 4.0.4 on 2022-06-21 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_alter_video_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='status',
            field=models.CharField(choices=[('PROCESSING', 'PROCESSING'), ('FAILED', 'FAILED'), ('COMPLETED', 'COMPLETED')], default='PROCESSING', max_length=12),
        ),
    ]
