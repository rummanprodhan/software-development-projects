# Generated by Django 5.1.3 on 2024-12-15 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_rename_status_accountvarification_accept_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountvarification',
            old_name='accept',
            new_name='status',
        ),
        migrations.RemoveField(
            model_name='accountvarification',
            name='decline',
        ),
    ]