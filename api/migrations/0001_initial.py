from django.db import migrations
from api.user.models import CustomUser

class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name='matias',
                          email='matias.traverso@gmail.com',
                          is_staff=True,
                          is_superuser=True,
                          phone='111111',
                          gender='Male'
                          )
        user.set_password("matias")
        user.save()

    dependencies = []

    operations = [
        migrations.RunPython(seed_data)
    ]