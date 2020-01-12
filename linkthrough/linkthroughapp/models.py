from django.db import models
import short_url

class Link(models.Model):
    url = models.CharField(
    	max_length = 255
    )

    def get_short_url(self):
    	return short_url.encode_url(self.pk)


    def __str__(self):
        return short_url.encode_url(self.pk)

class LinkVisit(models.Model):
    hashed_ip_address = models.CharField(
    	max_length = 56
    )
    time_visited = models.DateTimeField(
    	auto_now_add = True
    )
    link = models.ForeignKey(
    	'Link',
    	on_delete = models.CASCADE
    )

    def __str__(self):
        return self.hashed_ip_address
