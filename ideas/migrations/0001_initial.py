# Generated by Django 5.0.3 on 2024-04-09 07:26

import django.db.models.deletion
import django_jsonform.models.fields
import ideas.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('workspaces', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('content', models.TextField()),
                ('dimensions', django_jsonform.models.fields.JSONField(blank=True, default=dict)),
                ('votes_count', models.IntegerField(default=0)),
                ('priority', models.IntegerField(default=0)),
                ('formula', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=models.SET(ideas.models.get_deleted_user), related_name='ideas', to=settings.AUTH_USER_MODEL)),
                ('workspace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ideas', to='workspaces.workspace')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
