# Generated by Django 4.1.7 on 2023-06-02 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["publish"]},
        ),
    ]
