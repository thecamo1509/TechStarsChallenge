# Generated by Django 3.1.5 on 2021-01-20 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('day', models.CharField(max_length=200)),
                ('timeSlot', models.CharField(choices=[('AM', 'Morning'), ('PM', 'Afternoon')], max_length=50)),
                ('startup', models.ManyToManyField(to='app.Startup')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('meet', models.URLField()),
                ('status', models.CharField(max_length=50)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.mentor')),
                ('startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.startup')),
            ],
        ),
    ]
