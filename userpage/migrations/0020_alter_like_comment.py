# Generated by Django 3.2.12 on 2022-03-01 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0019_alter_like_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userpage.comment'),
        ),
    ]