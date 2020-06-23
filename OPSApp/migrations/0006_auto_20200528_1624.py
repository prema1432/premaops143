# Generated by Django 2.2.6 on 2020-05-28 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OPSApp', '0005_gstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='pupload',
            name='about',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pupload',
            name='comments',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pupload',
            name='pstatus',
            field=models.CharField(default='Pending', max_length=250),
        ),
        migrations.AddField(
            model_name='pupload',
            name='rating',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gstatus',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gstatus', to='OPSApp.pupload'),
        ),
    ]
