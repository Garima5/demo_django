# Generated by Django 3.2.5 on 2021-10-27 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.CharField(max_length=264)),
                ('beltA', models.IntegerField()),
                ('beltB', models.IntegerField()),
                ('beltC', models.IntegerField()),
                ('makingDate', models.DateField()),
            ],
        ),
    ]
