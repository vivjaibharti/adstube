from django.contrib import admin
from channel.models import Channel
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class ChannelAdmin(ImportExportModelAdmin):
    list_display=["channel_name","user","status"]

admin.site.register(Channel,ChannelAdmin)
