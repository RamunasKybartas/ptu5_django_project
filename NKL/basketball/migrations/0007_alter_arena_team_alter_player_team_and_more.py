# Generated by Django 4.1.4 on 2022-12-21 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basketball', '0006_team_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arena',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='arenas', to='basketball.team', verbose_name='team'),
        ),
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='players', to='basketball.team', verbose_name='team'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sponsors', to='basketball.team', verbose_name='team'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staffs', to='basketball.team', verbose_name='team'),
        ),
    ]
