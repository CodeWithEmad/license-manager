# Generated by Django 3.2.21 on 2023-09-18 04:32

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0057_auto_20230915_0722'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionLicenseSourceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=64)),
                ('slug', models.SlugField(max_length=30, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubscriptionLicenseSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('source_id', models.CharField(help_text='18 character value -- Salesforce Opportunity ID', max_length=18, validators=[django.core.validators.MinLengthValidator(18)])),
                ('license', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='source', to='subscriptions.license')),
                ('source_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscriptions.subscriptionlicensesourcetype')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
