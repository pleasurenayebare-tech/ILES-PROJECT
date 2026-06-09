from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            "ALTER TABLE accounts_customuser ALTER COLUMN department DROP NOT NULL;",
            "ALTER TABLE accounts_customuser ALTER COLUMN department SET NOT NULL;",
        ),
    ]
