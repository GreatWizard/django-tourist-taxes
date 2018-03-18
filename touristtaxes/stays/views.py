from django.views import View, generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Resident, Stay
import datetime


class StayListView(LoginRequiredMixin, generic.ListView):
    model = Stay

    def get_context_data(self, **kwargs):
        context = super(StayListView, self).get_context_data(**kwargs)
        now = datetime.datetime.now().date()
        locations = Resident.objects.filter(
          user=self.request.user,
          date_end__gte=now,
          date_begin__lte=now
        ).values('location').distinct()
        context['stay_list'] = Stay.objects.filter(
            user=self.request.user,
            is_validated=False,
            location__in=locations
        )
        context['stay_list_validated'] = Stay.objects.filter(
            user=self.request.user,
            is_validated=True,
            location__in=locations
        )
        return context


def validate_all(request):
    now = datetime.datetime.now().date()
    locations = Resident.objects.filter(
        user=request.user,
        date_end__gte=now,
        date_begin__lte=now
    ).values('location').distinct()
    Stay.objects.filter(
        user=request.user,
        is_validated=False,
        location__in=locations
    ).update(is_validated=True)
    return HttpResponseRedirect(reverse('stays'))
