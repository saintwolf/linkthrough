from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect
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
    try:
        id = short_url.decode_url(tiny)
    except ValueError:
        raise Http404('Bad encoded ID.')

    link = get_object_or_404(Link, pk=id)

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip_address = x_forwarded_for.split(',')[0]
    else:
        ip_address = request.META.get('REMOTE_ADDR')

    hash = hashlib.sha224(ip_address.encode('utf-8')).hexdigest()

    l = LinkVisit(hashed_ip_address=hash, link=link)
    l.save()

    return redirect(link.url)
