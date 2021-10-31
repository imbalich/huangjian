# Generated by Django 3.2.3 on 2021-10-30 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='t_naodu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naodu_1', models.CharField(blank=True, max_length=64, null=True, verbose_name='1号测量点挠度值')),
                ('naodu_2', models.CharField(blank=True, max_length=64, null=True, verbose_name='2号测量点挠度值')),
                ('naodu_3', models.CharField(blank=True, max_length=64, null=True, verbose_name='3号测量点挠度值')),
                ('naodu_4', models.CharField(blank=True, max_length=64, null=True, verbose_name='4号测量点挠度值')),
                ('naodu_5', models.CharField(blank=True, max_length=64, null=True, verbose_name='5号测量点挠度值')),
                ('y_time', models.CharField(blank=True, max_length=64, null=True, verbose_name='挠度记录时间')),
            ],
        ),
        migrations.CreateModel(
            name='t_wendu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wendu_1', models.CharField(blank=True, max_length=64, null=True, verbose_name='1号测量点温度值')),
                ('wendu_2', models.CharField(blank=True, max_length=64, null=True, verbose_name='2号测量点温度值')),
                ('wendu_3', models.CharField(blank=True, max_length=64, null=True, verbose_name='3号测量点温度值')),
                ('wendu_4', models.CharField(blank=True, max_length=64, null=True, verbose_name='4号测量点温度值')),
                ('wendu_5', models.CharField(blank=True, max_length=64, null=True, verbose_name='5号测量点温度值')),
                ('y_time', models.CharField(blank=True, max_length=64, null=True, verbose_name='温度记录时间')),
            ],
        ),
        migrations.CreateModel(
            name='t_xiushi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xiushi_1', models.CharField(blank=True, max_length=64, null=True, verbose_name='1号测量点锈蚀值')),
                ('xiushi_2', models.CharField(blank=True, max_length=64, null=True, verbose_name='2号测量点锈蚀值')),
                ('xiushi_3', models.CharField(blank=True, max_length=64, null=True, verbose_name='3号测量点锈蚀值')),
                ('xiushi_4', models.CharField(blank=True, max_length=64, null=True, verbose_name='4号测量点锈蚀值')),
                ('xiushi_5', models.CharField(blank=True, max_length=64, null=True, verbose_name='5号测量点锈蚀值')),
                ('y_time', models.CharField(blank=True, max_length=64, null=True, verbose_name='锈蚀记录时间')),
            ],
        ),
        migrations.CreateModel(
            name='t_yingbian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yingbian_1', models.CharField(blank=True, max_length=64, null=True, verbose_name='1号测量点应变值')),
                ('yingbian_2', models.CharField(blank=True, max_length=64, null=True, verbose_name='2号测量点应变值')),
                ('yingbian_3', models.CharField(blank=True, max_length=64, null=True, verbose_name='3号测量点应变值')),
                ('yingbian_4', models.CharField(blank=True, max_length=64, null=True, verbose_name='4号测量点应变值')),
                ('yingbian_5', models.CharField(blank=True, max_length=64, null=True, verbose_name='5号测量点应变值')),
                ('y_time', models.CharField(blank=True, max_length=64, null=True, verbose_name='应变记录时间')),
            ],
        ),
        migrations.CreateModel(
            name='t_yujing_nd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('y_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='挠度超警位置')),
                ('y_shuzhi', models.CharField(blank=True, max_length=64, null=True, verbose_name='挠度超警数值')),
                ('y_time', models.CharField(blank=True, max_length=64, null=True, verbose_name='挠度超警记录时间')),
            ],
        ),
        migrations.CreateModel(
            name='t_yujing_wd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('y_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='温度超警位置')),
                ('y_shuzhi', models.CharField(blank=True, max_length=64, null=True, verbose_name='温度超警数值')),
                ('y_time', models.CharField(blank=True, max_length=64, null=True, verbose_name='温度超警记录时间')),
            ],
        ),
        migrations.CreateModel(
            name='t_yujing_xs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('y_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='锈蚀超警位置')),
                ('y_shuzhi', models.CharField(blank=True, max_length=64, null=True, verbose_name='锈蚀超警数值')),
                ('y_time', models.CharField(blank=True, max_length=64, null=True, verbose_name='锈蚀超警记录时间')),
            ],
        ),
        migrations.CreateModel(
            name='t_yujing_yb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('y_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='应变超警位置')),
                ('y_shuzhi', models.CharField(blank=True, max_length=64, null=True, verbose_name='应变超警数值')),
                ('y_time', models.CharField(blank=True, max_length=64, null=True, verbose_name='应变超警记录时间')),
            ],
        ),
    ]
