# Generated by Django 3.1.7 on 2021-06-21 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.TextField()),
                ('name', models.TextField()),
                ('sys_argv', models.TextField(null=True, verbose_name='sys.argv')),
                ('args', models.TextField(null=True)),
                ('options', models.TextField(null=True)),
                ('is_success', models.BooleanField(verbose_name='success')),
                ('stdout', models.TextField(null=True)),
                ('hostname', models.TextField(null=True)),
                ('cpu_time', models.FloatField(default=0.0)),
                ('mem_before', models.FloatField(verbose_name='mem before')),
                ('mem_after', models.FloatField(verbose_name='mem after')),
                ('queries_count', models.TextField(verbose_name='queries')),
                ('exc_type', models.TextField(null=True)),
                ('exc_value', models.TextField(null=True)),
                ('exc_traceback', models.TextField(null=True)),
                ('started_at', models.DateTimeField(verbose_name='started')),
                ('finished_at', models.DateTimeField(verbose_name='finished')),
            ],
            options={
                'db_table': 'django_command_stat_call',
                'ordering': ('-started_at',),
            },
        ),
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.TextField()),
                ('name', models.TextField(unique=True)),
                ('is_success', models.BooleanField(null=True, verbose_name='success')),
                ('is_running', models.BooleanField(null=True, verbose_name='running')),
                ('pid', models.IntegerField(null=True)),
                ('cpu_time', models.FloatField(null=True)),
                ('mem_before', models.FloatField(null=True, verbose_name='mem before')),
                ('mem_after', models.FloatField(null=True, verbose_name='mem after')),
                ('calls_count', models.IntegerField(default=1, verbose_name='calls')),
                ('errors_count', models.IntegerField(default=0, verbose_name='errors')),
                ('started_at', models.DateTimeField(null=True, verbose_name='started')),
                ('finished_at', models.DateTimeField(null=True, verbose_name='finished')),
            ],
            options={
                'db_table': 'django_command_stat_command',
                'ordering': ('name',),
            },
        ),
        migrations.AddIndex(
            model_name='command',
            index=models.Index(fields=['app'], name='django_comm_app_4653b4_idx'),
        ),
        migrations.AddIndex(
            model_name='command',
            index=models.Index(fields=['name'], name='django_comm_name_00e944_idx'),
        ),
        migrations.AddIndex(
            model_name='command',
            index=models.Index(fields=['is_running'], name='django_comm_is_runn_2a4770_idx'),
        ),
        migrations.AddIndex(
            model_name='command',
            index=models.Index(fields=['is_success'], name='django_comm_is_succ_e7ff87_idx'),
        ),
        migrations.AddIndex(
            model_name='command',
            index=models.Index(fields=['-finished_at'], name='django_comm_finishe_bb7a9a_idx'),
        ),
        migrations.AddIndex(
            model_name='call',
            index=models.Index(fields=['app'], name='django_comm_app_368fb5_idx'),
        ),
        migrations.AddIndex(
            model_name='call',
            index=models.Index(fields=['name'], name='django_comm_name_83a7b3_idx'),
        ),
        migrations.AddIndex(
            model_name='call',
            index=models.Index(fields=['is_success'], name='django_comm_is_succ_2f02e8_idx'),
        ),
        migrations.AddIndex(
            model_name='call',
            index=models.Index(fields=['exc_type'], name='django_comm_exc_typ_44f9c1_idx'),
        ),
        migrations.AddIndex(
            model_name='call',
            index=models.Index(fields=['-started_at'], name='django_comm_started_94019d_idx'),
        ),
    ]