# Generated by Django 4.1.1 on 2022-10-06 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_model', '0002_alter_student_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
    ]