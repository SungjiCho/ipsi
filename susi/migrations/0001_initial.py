# Generated by Django 3.0.5 on 2020-04-30 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Susi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31, verbose_name='전형명')),
                ('year', models.IntegerField(choices=[(1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021)], verbose_name='학년도')),
                ('susi_type', models.CharField(choices=[('HJ', '학생부 종합전형'), ('HG', '학생부 교과전형'), ('NS', '논술전형'), ('SG', '실기전형'), ('GG', '기회균등전형')], max_length=31, verbose_name='전형 종류')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.University', verbose_name='대학')),
            ],
        ),
        migrations.CreateModel(
            name='SusiDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('required_documents', models.TextField(blank=True, verbose_name='필요 서류')),
                ('min_grade', models.TextField(verbose_name='수능 최저등급')),
                ('major', models.ManyToManyField(to='university.Major', verbose_name='학과')),
                ('susi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='susi.Susi', verbose_name='수시전형')),
            ],
        ),
        migrations.CreateModel(
            name='SusiSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255, verbose_name='설명')),
                ('start_date', models.DateTimeField(verbose_name='시작시간')),
                ('end_date', models.DateTimeField(verbose_name='종료시간')),
                ('susi_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='susi.SusiDetail', verbose_name='수시전형 종류')),
            ],
        ),
    ]
