from django.views import generic
from .models import Owner, Stay
import datetime


class StayListView(generic.ListView):
    model = Stay

    def get_queryset(self):
        now = datetime.datetime.now().date()
        locations = Owner.objects.filter(
          user=self.request.user,
          date_end__gte=now,
          date_begin__lte=now
        ).values('location').distinct()
        return Stay.objects.filter(location__in=locations)
