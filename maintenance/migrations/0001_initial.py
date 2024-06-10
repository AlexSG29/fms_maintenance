# Generated by Django 4.2 on 2024-06-10 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contact', '0002_alter_contact_address_alter_contact_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_plate', models.CharField(max_length=8)),
                ('maintenance_type', models.CharField(choices=[('Correctivo', 'Correctivo'), ('Predictivo', 'Predictivo')], max_length=20)),
                ('work_order', models.CharField(max_length=100)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('description', models.TextField()),
                ('parts_replaced', models.TextField()),
                ('completed', models.BooleanField(default=False)),
                ('workers', models.ManyToManyField(to='contact.contact')),
            ],
        ),
    ]
