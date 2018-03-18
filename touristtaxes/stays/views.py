from django.shortcuts import render
from .models import Owner, Stay
import datetime


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    now = datetime.datetime.now()
    locations = Owner.objects.filter(
      user=request.user,
      date_end__gte=now.date(),
      date_begin__lte=now.date()
    ).values('location').distinct()
    stays = Stay.objects.filter(location__in=locations)

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={
            'num_location': locations.count(),
            'num_stay': stays.count()
        },
    )
