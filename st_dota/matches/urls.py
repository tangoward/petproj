
from django.urls import path
from . import views


app_name = 'matches'

urlpatterns = [
	path('', views.DotaMatches.as_view(), name='dota_matches')
]