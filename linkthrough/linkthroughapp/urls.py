from django.urls import path

from . import views

app_name = 'linkthroughapp'
urlpatterns = [
	path('<tiny>/', views.redirect_view, name='short_url_view'),
    path('', views.index, name='index'),
]
