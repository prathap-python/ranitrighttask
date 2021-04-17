from django.contrib import admin
from task.models import Details,Search,GetImages
class DetailAdmin(admin.ModelAdmin):
    list_display=["Name","Url","Phonenumber"]
class SearchAdmin(admin.ModelAdmin):
    list_display=["SearchedName"]
class GetImagesAdmin(admin.ModelAdmin):
    list_display=["EnteredLink"]
admin.site.register(Details,DetailAdmin)
admin.site.register(Search,SearchAdmin)
admin.site.register(GetImages,GetImagesAdmin)

# Register your models here.
