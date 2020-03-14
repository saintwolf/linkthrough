from django.contrib import admin
from linkthroughapp.models import Link, LinkVisit

class LinkAdmin(admin.ModelAdmin):
	list_display = ('get_short_url', 'name', 'url')

class LinkVisitAdmin(admin.ModelAdmin):
	list_display = ('hashed_ip_address', 'time_visited')
	def link_link(self, obj):
		return mark_safe('<a href="{}">{}</a>'.format(
		reverse("admin:link_change", args=(obj.link.pk,)),
			obj.link.url
        ))

admin.site.register(Link, LinkAdmin)
admin.site.register(LinkVisit)
