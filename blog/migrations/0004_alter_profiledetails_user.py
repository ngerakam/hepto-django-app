# Generated by Django 4.1.4 on 2022-12-27 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_author_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiledetails',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.author'),
        ),
    ]