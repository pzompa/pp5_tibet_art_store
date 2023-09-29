# Generated by Django 3.2.20 on 2023-09-28 16:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comment', '0002_productcomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPostComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254)),
                ('blogpost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogpost.blogpost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
