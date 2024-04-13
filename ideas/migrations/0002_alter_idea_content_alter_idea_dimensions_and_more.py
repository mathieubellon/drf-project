# Generated by Django 5.0.3 on 2024-04-12 05:50

import django.db.models.deletion
import django_jsonform.models.fields
import ideas.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0001_initial'),
        ('workspaces', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='idea',
            name='dimensions',
            field=django_jsonform.models.fields.JSONField(default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='idea',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='idea',
            name='priority',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='idea',
            name='votes_count',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.CreateModel(
            name='Formula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=models.SET(ideas.models.get_deleted_user), related_name='formulas', to=settings.AUTH_USER_MODEL)),
                ('workspace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='formulas', to='workspaces.workspace')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
