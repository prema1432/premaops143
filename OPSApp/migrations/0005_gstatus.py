# Generated by Django 2.2.6 on 2020-05-28 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OPSApp', '0004_pupload_ereport'),
    ]

    operations = [
        migrations.CreateModel(
            name='gstatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pstatus', models.CharField(default='Pending', max_length=250)),
                ('comments', models.TextField()),
                ('about', models.TextField()),
                ('rating', models.CharField(max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OPSApp.pupload')),
            ],
        ),
    ]
