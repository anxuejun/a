from django.contrib import admin

# Register your models here.

import models

class AssetAdmin(admin.ModelAdmin):
 #   def get_group_name(self,obj):
  #      if obj.server_group:
   #         return obj.server_group.group_name
    #    else:
     #       return 'not in any group'
#    list_display = ('id','get_asset_type_display','asset_num','asset_configuration')
    list_display = ('id','asset_username','asset_postation','asset_cable_ip','get_asset_type_display','asset_num','asset_configuration')
    search_fields = ('asset_username','asset_postation','asset_cable_ip','asset_num','asset_configuration')
    list_filter = ('asset_type','asset_postation','asset_configuration')
    list_per_page = 25
    ordering = ['-id']

class ShinesAdmin(admin.ModelAdmin):
     list_display = ('id','shines_notes','shines_neiwang_ip','shines_waiwang_ip')

admin.site.register(models.UserProfile_Name)
admin.site.register(models.Group)
admin.site.register(models.Asset,AssetAdmin)

admin.site.register(models.Shines,ShinesAdmin)

