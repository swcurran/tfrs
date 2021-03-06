# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-16 20:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20171102_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fuelsupplierattachmenttag',
            name='create_user',
        ),
        migrations.RemoveField(
            model_name='fuelsupplierattachmenttag',
            name='fuelSupplierAttachmentFK',
        ),
        migrations.RemoveField(
            model_name='fuelsupplierattachmenttag',
            name='update_user',
        ),
        migrations.RemoveField(
            model_name='fuelsupplierccdata',
            name='create_user',
        ),
        migrations.RemoveField(
            model_name='fuelsupplierccdata',
            name='fuelSupplierFK',
        ),
        migrations.RemoveField(
            model_name='fuelsupplierccdata',
            name='update_user',
        ),
        migrations.RemoveField(
            model_name='fuelsuppliercontact',
            name='create_user',
        ),
        migrations.RemoveField(
            model_name='fuelsuppliercontact',
            name='fuelSupplierFK',
        ),
        migrations.RemoveField(
            model_name='fuelsuppliercontact',
            name='update_user',
        ),
        migrations.RemoveField(
            model_name='fuelsuppliercontact',
            name='userFK',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='create_user',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='notificationEventFK',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='update_user',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='userFK',
        ),
        migrations.RemoveField(
            model_name='notificationevent',
            name='create_user',
        ),
        migrations.RemoveField(
            model_name='notificationevent',
            name='creditTradeFK',
        ),
        migrations.RemoveField(
            model_name='notificationevent',
            name='update_user',
        ),
        migrations.RemoveField(
            model_name='notificationtype',
            name='create_user',
        ),
        migrations.RemoveField(
            model_name='notificationtype',
            name='update_user',
        ),
        migrations.RenameField(
            model_name='credittradestatus',
            old_name='expirationDate',
            new_name='expiration_date',
        ),
        migrations.RenameField(
            model_name='credittradetype',
            old_name='expirationDate',
            new_name='expiration_date',
        ),
        migrations.RenameField(
            model_name='credittradezeroreason',
            old_name='expirationDate',
            new_name='expiration_date',
        ),
        migrations.RenameField(
            model_name='fuelsupplieractionstype',
            old_name='expirationDate',
            new_name='expiration_date',
        ),
        migrations.RenameField(
            model_name='fuelsupplierbalance',
            old_name='endDate',
            new_name='expiration_date',
        ),
        migrations.RenameField(
            model_name='fuelsupplierstatus',
            old_name='expirationDate',
            new_name='expiration_date',
        ),
        migrations.DeleteModel(
            name='FuelSupplierAttachmentTag',
        ),
        migrations.DeleteModel(
            name='FuelSupplierCCData',
        ),
        migrations.DeleteModel(
            name='FuelSupplierContact',
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
        migrations.DeleteModel(
            name='NotificationEvent',
        ),
        migrations.DeleteModel(
            name='NotificationType',
        ),
    ]
