from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20200711_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='listingid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
