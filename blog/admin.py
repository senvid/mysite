from django.contrib import admin

# Register your models here.
from blog.models import blogAdmin, entries

admin.site.register(entries,blogAdmin)
