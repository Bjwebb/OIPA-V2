# Django specific
from django.conf import settings
from django.template.response import TemplateResponse

# Api specific
from api.v2.resources.model_resources import ActivityResource
from api.v2.resources.model_resources import OrganisationResource
from api.v2.resources.common_model_resources import CountryResource
from api.v2.resources.common_model_resources import RegionResource
from api.v2.resources.common_model_resources import SectorResource


def docs_index(request):
    context = dict()
    context['title'] = 'Documentation'
    t = TemplateResponse(request, 'base.html', context)
    return t.render()

def docs_start(request):
    context = dict()
    context['title'] = 'Getting started'
    t = TemplateResponse(request, 'documentation/start.html', context)
    return t.render()

def docs_resources(request):
    context = dict()
    context['title'] = 'Resources'
    context['resources'] = dict(
        organisation = OrganisationResource.__name__,
        organisation_doc = OrganisationResource.__doc__,
        activity = ActivityResource.__name__,
        activity_doc = ActivityResource.__doc__,
        country = CountryResource.__name__,
        country_doc = CountryResource.__doc__,
        region = RegionResource.__name__,
        region_doc = RegionResource.__doc__,
        sector = SectorResource.__name__,
        sector_doc = SectorResource.__doc__,
    )
    t = TemplateResponse(request, 'documentation/resources.html', context)
    return t.render()

def docs_filtering(request):
    context = dict()
    context['title'] = 'Filtering'
    t = TemplateResponse(request, 'documentation/filtering.html', context)
    return t.render()

def docs_ordering(request):
    context = dict()
    context['title'] = 'Ordering'
    t = TemplateResponse(request, 'documentation/ordering.html', context)
    return t.render()
