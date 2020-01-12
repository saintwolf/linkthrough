from django.contrib import admin
from linkthroughapp.models import Link, LinkVisit

class LinkAdmin(admin.ModelAdmin):
	list_display = ('get_short_url', 'url')

admin.site.register(Link, LinkAdmin)
admin.site.register(LinkVisit)
