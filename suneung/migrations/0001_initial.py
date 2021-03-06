# Generated by Django 3.0.5 on 2020-06-05 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suneung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255, verbose_name='설명')),
                ('start_date', models.DateTimeField(verbose_name='시작시간')),
                ('end_date', models.DateTimeField(verbose_name='종료시간')),
            ],
            options={
                'verbose_name': '수능 및 모의고사 일정',
                'verbose_name_plural': '수능 및 모의고사 일정',
            },
        ),
    ]
