# Generated by Django 4.1.1 on 2022-10-01 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hirer', '0003_alter_candidature_opportunity_alter_candidature_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidature',
            name='resume_url',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]