# Generated by Django 5.2.1 on 2025-05-10 20:35

from django.db import migrations


def populate_role(apps, schemaeditor):
    entries = {
        "developer": "The person on the team who works on issues",
        "scrum master": "The team's coach",
        "product owner": "The person on the team who defines issues"
    }
    Role = apps.get_model("accounts", "Role")
    for key, value in entries.items():
        role_obj = Role(name=key, description=value)
        role_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_role)
    ]
