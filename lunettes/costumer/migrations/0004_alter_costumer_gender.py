# Generated by Django 4.0.4 on 2022-04-28 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('costumer', '0003_costumer_image_alter_costumer_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costumer',
            name='gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='costumer.gender'),
        ),
    ]
