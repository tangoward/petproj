
from django.views.generic import ListView, DetailView
from .models import Region_Name
# Create your views here.


class RegionList(ListView):
    model = Region_Name
    context_object_name = 'region_list'
    template_name = 'teams/region_list.html'


class RegionDetail(DetailView):
    model = Region_Name
    context_object_name = 'region_detail'
    template_name = 'teams/region_detail.html'
