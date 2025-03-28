# Generated by Django 3.2.25 on 2025-03-11 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_alter_itemvariation_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemvariation',
            name='uid',
            field=models.BigIntegerField(db_index=True, null=True, unique=True),
        ),
        migrations.AddConstraint(
            model_name='itemvariation',
            constraint=models.UniqueConstraint(condition=models.Q(('uid__isnull', False)), fields=('uid',), name='unique_non_null_uid'),
        ),
    ]
