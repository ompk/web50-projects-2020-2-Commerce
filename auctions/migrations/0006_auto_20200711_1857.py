
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20200711_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='link',
            field=models.CharField(default='https://wallpaperaccess.com/full/1605486.jpg', max_length=64),
        ),
    ]
