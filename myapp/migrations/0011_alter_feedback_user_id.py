# Generated by Django 4.2 on 2023-05-17 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_feedback_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.register'),
        ),
    ]
