# Generated by Django 3.0.5 on 2020-04-30 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31, unique=True, verbose_name='단과대명')),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31, unique=True, verbose_name='대학명')),
                ('logo', models.ImageField(blank=True, upload_to='university/logo', verbose_name='대학 로고')),
                ('region', models.CharField(choices=[('S', '서울'), ('GI', '경인'), ('GW', '강원'), ('CC', '충청'), ('GS', '경상'), ('JL', '전라'), ('JJ', '제주')], max_length=31, verbose_name='소재 지역')),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31, unique=True, verbose_name='학과명')),
                ('moonigwa', models.CharField(choices=[('MG', '문과'), ('IG', '이과'), ('YCN', '예체능')], max_length=7, verbose_name='계열')),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.College', verbose_name='소속 단과대')),
            ],
        ),
        migrations.AddField(
            model_name='college',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.University', verbose_name='소속 대학'),
        ),
    ]
