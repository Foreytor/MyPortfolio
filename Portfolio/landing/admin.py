from django.contrib import admin

from .models import HeaderHome, ContentSlidebar, ContensBar, ContentServices, \
                    ContentWorks, SettingSidebar, ContentFooter

# Register your models here.
admin.site.register(HeaderHome)
admin.site.register(ContentSlidebar)
admin.site.register(ContensBar)
admin.site.register(ContentServices)
admin.site.register(ContentWorks)
admin.site.register(SettingSidebar)
admin.site.register(ContentFooter)