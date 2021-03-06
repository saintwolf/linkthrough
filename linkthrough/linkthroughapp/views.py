from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
import hashlib
import short_url

from .models import Link, LinkVisit

def index(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

	if x_forwarded_for:
		ip_address = x_forwarded_for.split(',')[0]
	else:
		ip_address = request.META.get('REMOTE_ADDR')

	hash = hashlib.sha224(ip_address.encode('utf-8')).hexdigest()

	l = LinkVisit(hashed_ip_address=hash)
	l.save()

	return HttpResponse("IP is: {}<br />Hash is: {}".format(ip_address, hash))

def redirect_view(request, tiny):
	link = get_link_from_short(tiny)

	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

	if x_forwarded_for:
		ip_address = x_forwarded_for.split(',')[0]
	else:
		ip_address = request.META.get('REMOTE_ADDR')

	hash = hashlib.sha224(ip_address.encode('utf-8')).hexdigest()

	l = LinkVisit(hashed_ip_address=hash, link=link)
	l.save()

	return redirect(link.url)

def link_stats_view(request, tiny):

	link = get_link_from_short(tiny)

	visit_count = link.visits.count()
	unique_visit_count = link.visits.values('hashed_ip_address').distinct().order_by().count()
	link_visits = link.visits.order_by('-time_visited')
	context = {
		'link_visits': link_visits,
		'visit_count': visit_count,
		'unique_visit_count': unique_visit_count
	}

	#return HttpResponse("Total Redirects: {}<br />Unique Redirects: {}".format(visit_count, unique_visit_count))
	return render(request, 'linkthroughapp/link_stats_view.html', context)

def get_link_from_short(tiny):
	try:
		id = short_url.decode_url(tiny)
	except ValueError:
		raise Http404('Bad encoded ID.')

	link = get_object_or_404(Link, pk=id)
	return link
