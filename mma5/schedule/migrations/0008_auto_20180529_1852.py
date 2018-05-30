# Generated by Django 2.0.5 on 2018-05-29 18:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0007_auto_20180529_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inst',
            name='loan_student',
            field=models.ForeignKey(blank=True, default=1, limit_choices_to={'groups__name': 'Student'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='loan_student', to=settings.AUTH_USER_MODEL),
        ),
    ]
