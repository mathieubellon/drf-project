# Generated by Django 5.0.3 on 2024-04-07 16:35

import workspaces.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspaces', '0002_alter_workspace_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='workspace',
            name='members',
            field=models.ManyToManyField(related_name='workspaces', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='owner',
            field=models.ForeignKey(on_delete=models.SET(workspaces.models.get_deleted_user), related_name='workspace_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]