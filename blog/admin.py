from django.contrib import admin

# Register your models here.
from blog.models import entries


class blogAdmin(admin.ModelAdmin):
    fieldsets = [
        ("TITLE", {"fields": ["title"]}),
        ("MARKDOWN", {"fields": ["markdown"]}),
        ("published", {"fields": ["published"]})
    ]

    list_display = ("slug", "title", "published", "updated")

    list_filter = ["published"]
    search_fields = ["title"]

admin.site.register(entries, blogAdmin)
