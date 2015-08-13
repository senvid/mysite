from django.contrib import admin

# Register your models here.
from blog.models import entries

class blogAdmin(admin.ModelAdmin):
    fieldsets = [
    	("TITLE",{"fields":["title"]}),
    	("HTML",{"fields":["html"]}),
    	("published",{"fields:["published"]})
    	]

	#list_display = ("title","published","updated")


admin.site.register(entries,blogAdmin)
