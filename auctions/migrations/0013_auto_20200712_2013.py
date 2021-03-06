from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_auto_20200712_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='closedbid',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='closedbid',
            name='link',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='closedbid',
            name='time',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='closedbid',
            name='title',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
