from django.views import generic
from .models import Resident, Stay
import datetime


class StayListView(generic.ListView):
    model = Stay

    def get_queryset(self):
        now = datetime.datetime.now().date()
        locations = Resident.objects.filter(
            user=self.request.user,
            date_end__gte=now,
            date_begin__lte=now
        ).values('location').distinct()
        return Stay.objects.filter(
            is_validated=False,
            location__in=locations
        )

    def get_context_data(self, **kwargs):
        context = super(StayListView, self).get_context_data(**kwargs)
        now = datetime.datetime.now().date()
        locations = Resident.objects.filter(
          user=self.request.user,
          date_end__gte=now,
          date_begin__lte=now
        ).values('location').distinct()
        context['stay_list_validated'] = Stay.objects.filter(
            is_validated=True,
            location__in=locations
        )
        return context
