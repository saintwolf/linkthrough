from django.urls import path

from . import views

app_name = 'linkthroughapp'
urlpatterns = [
	path('<tiny>/stats', views.link_stats_view, name='link_stats_view'),
	path('<tiny>/', views.redirect_view, name='short_url_view'),
]
