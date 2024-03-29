# Generated by Django 3.2.7 on 2021-10-19 21:46

from django.db import migrations

def create_profile(apps, schema_migration):
    User = apps.get_model('auth', 'User')
    Profile = apps.get_model('commercial', 'Profile')
    Departament = apps.get_model('commercial', 'Departament')

    departament = Departament.objects.first()
    for user in User.objects.filter(profile__isnull=True):
        Profile.objects.create(
            user=user,
            department=departament
        )

class Migration(migrations.Migration):

    dependencies = [
        ('commercial', '0007_startpageimage_department_order'),
    ]

    operations = [
        migrations.RunPython(create_profile, reverse_code=migrations.RunPython.noop)
    ]
