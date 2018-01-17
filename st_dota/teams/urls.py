from django.urls import path
from . import views


# namespace
app_name = 'teams'

urlpatterns = [
    path('', views.RegionList.as_view(), name='region_list'),
    path('<int:pk>/', views.RegionDetail.as_view(), name='region_detail'),
]
