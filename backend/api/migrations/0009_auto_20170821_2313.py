# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-21 23:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20170817_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='audit',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='audit',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_audit_CREATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='audit',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='audit',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_audit_UPDATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='credittrade',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='credittrade',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_credittrade_CREATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='credittrade',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='credittrade',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_credittrade_UPDATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='credittradehistory',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='credittradehistory',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_credittradehistory_CREATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='credittradehistory',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='credittradehistory',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_credittradehistory_UPDATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='credittradestatus',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='credittradestatus',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_credittradestatus_CREATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='credittradestatus',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='credittradestatus',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_credittradestatus_UPDATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='credittradetype',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='credittradetype',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_credittradetype_CREATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='credittradetype',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='credittradetype',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_credittradetype_UPDATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='fuelsupplier',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsupplier',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_fuelsupplier_CREATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='fuelsupplier',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsupplier',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_fuelsupplier_UPDATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='fuelsupplieractionstype',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsupplieractionstype',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_fuelsupplieractionstype_CREATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='fuelsupplieractionstype',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsupplieractionstype',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_fuelsupplieractionstype_UPDATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='fuelsupplierattachment',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsupplierattachment',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_fuelsupplierattachment_CREATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='fuelsupplierattachment',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsupplierattachment',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_fuelsupplierattachment_UPDATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='fuelsupplierattachmenttag',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsupplierattachmenttag',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_fuelsupplierattachmenttag_CREATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='fuelsupplierattachmenttag',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsupplierattachmenttag',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_fuelsupplierattachmenttag_UPDATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='fuelsupplierbalance',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsupplierbalance',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_fuelsupplierbalance_CREATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='fuelsupplierbalance',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsupplierbalance',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_fuelsupplierbalance_UPDATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='fuelsupplierccdata',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsupplierccdata',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_fuelsupplierccdata_CREATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='fuelsupplierccdata',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsupplierccdata',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_fuelsupplierccdata_UPDATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='fuelsuppliercontact',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsuppliercontact',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_fuelsuppliercontact_CREATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='fuelsuppliercontact',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsuppliercontact',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_fuelsuppliercontact_UPDATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='fuelsuppliercontactrole',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsuppliercontactrole',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_fuelsuppliercontactrole_CREATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='fuelsuppliercontactrole',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsuppliercontactrole',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_fuelsuppliercontactrole_UPDATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='fuelsupplierhistory',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsupplierhistory',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_fuelsupplierhistory_CREATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='fuelsupplierhistory',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsupplierhistory',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_fuelsupplierhistory_UPDATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='fuelsupplierstatus',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsupplierstatus',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_fuelsupplierstatus_CREATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='fuelsupplierstatus',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsupplierstatus',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_fuelsupplierstatus_UPDATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='fuelsuppliertype',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsuppliertype',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_fuelsuppliertype_CREATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='fuelsuppliertype',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelsuppliertype',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_fuelsuppliertype_UPDATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='notification',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_notification_CREATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='notification',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_notification_UPDATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='notificationevent',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='notificationevent',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_notificationevent_CREATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='notificationevent',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='notificationevent',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_notificationevent_UPDATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='notificationtype',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='notificationtype',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_notificationtype_CREATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='notificationtype',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='notificationtype',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_notificationtype_UPDATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='opportunity',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='opportunity',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_opportunity_CREATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='opportunity',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='opportunity',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_opportunity_UPDATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='opportunityhistory',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='opportunityhistory',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_opportunityhistory_CREATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='opportunityhistory',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='opportunityhistory',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_opportunityhistory_UPDATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='opportunitystatus',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='opportunitystatus',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_opportunitystatus_CREATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='opportunitystatus',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='opportunitystatus',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_opportunitystatus_UPDATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='permission',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='permission',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_permission_CREATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='permission',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='permission',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_permission_UPDATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='role',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='role',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_role_CREATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='role',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='role',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_role_UPDATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='rolepermission',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='rolepermission',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_rolepermission_CREATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='rolepermission',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='rolepermission',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_rolepermission_UPDATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='user',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_user_CREATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='user',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_user_UPDATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='userfavourite',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='userfavourite',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_userfavourite_CREATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='userfavourite',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='userfavourite',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_userfavourite_UPDATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='userrole',
            name='CREATE_TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='userrole',
            name='CREATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_userrole_CREATE_USER', to='api.User'),
        ),
        migrations.AddField(
            model_name='userrole',
            name='UPDATE_TIMESTAMP',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='userrole',
            name='UPDATE_USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_userrole_UPDATE_USER', to='api.User'),
        ),
    ]
