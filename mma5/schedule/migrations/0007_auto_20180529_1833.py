# Generated by Django 2.0.5 on 2018-05-29 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0006_auto_20180529_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='lesson_instrument',
            field=models.CharField(choices=[('Guitar', 'Guitar'), ('Drums', 'Drums'), ('Violin', 'Violin'), ('Saxophone', 'Saxophone'), ('Clarinet', 'Clarinet'), ('Piano', 'Piano'), ('Vocals', 'Vocals'), ('Cello', 'Cello')], default='Guitar', max_length=20),
        ),
    ]
