from django.contrib import admin

from emailcampaign.models import *


class CampaignAdmin(admin.ModelAdmin):
    pass

admin.site.register(Campaign, CampaignAdmin)


class ContactListAdmin(admin.ModelAdmin):
    pass

admin.site.register(ContactList, CampaignAdmin)


class ContactAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contact, ContactAdmin)


