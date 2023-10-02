# Generated by Django 4.2.5 on 2023-10-02 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_gid', models.CharField(max_length=100)),
                ('task_name', models.CharField(max_length=100)),
                ('task_note', models.CharField(blank=True, max_length=100, null=True)),
                ('task_section', models.CharField(max_length=100)),
                ('task_section_gid', models.CharField(max_length=100)),
            ],
        ),
    ]
